# train_ddp.py
import os
import sys
import re
from contextlib import contextmanager

import torch
import torch.distributed as dist
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.tensorboard import SummaryWriter

# Hugging Face / PEFT
from transformers import get_scheduler

# Utilities
import librosa
import json
import math
import random
import numpy as np
import scipy.signal
import soundfile as sf
from tqdm import tqdm
from structure_derivation.helpers.utils import setup_distributed, read_jsonl_files
from structure_derivation.model.model import StructureDerivationModel, StructureDerivationModelConfig
from training_config import *


@contextmanager
def suppress_stderr():
    """A context manager to temporarily redirect stderr."""
    original_stderr_fd = sys.stderr.fileno()
    devnull_fd = os.open(os.devnull, os.O_WRONLY)

    # Save original and redirect
    original_stderr_dup = os.dup(original_stderr_fd)
    os.dup2(devnull_fd, original_stderr_fd)

    try:
        yield
    finally:
        # Restore original stderr
        os.dup2(original_stderr_dup, original_stderr_fd)
        os.close(devnull_fd)
        os.close(original_stderr_dup)

# -----------------------
# Audio Text Dataset
# -----------------------
class AudioTextDataset(Dataset):
    def __init__(self, data, split="train"):
        self.data = data
        self.split = split
        if self.split == "train":
            random.seed(42)
            random.shuffle(self.data)
        self.sr = 24000  # Target sampling rate
        print(f"Initializing {split} dataset with {len(self.data)} samples")

    def __len__(self):
        return len(self.data)

    def on_epoch_end(self):
        if self.split == "train":
            random.shuffle(self.data)

    def read_audio(self, audio_path):
        """
        Read an audio file and return two non-overlapping random segments.
        Each segment duration is between 5s and 30s.
        Assumes total audio is at least 30s long (or at least 2 * min_dur).
        """
        min_dur = 5.0   # seconds
        max_dur = MAX_AUDIO_LEN  # seconds

        # 1) Get total duration
        with suppress_stderr():
            total_duration = librosa.get_duration(path=audio_path)
        if total_duration < (2 * min_dur):
            raise ValueError(f"Audio {audio_path} too short for 2 segments.")

        # 2) Choose dur1 so that at least min_dur remains for dur2
        dur1_upper = min(max_dur, total_duration - min_dur)
        dur1 = random.uniform(min_dur, dur1_upper)

        # 3) Choose dur2 so that dur1 + dur2 <= total_duration
        dur2_upper = min(max_dur, total_duration - dur1)
        dur2 = random.uniform(min_dur, dur2_upper)

        # 4) Try to place start1 randomly, then find a valid non-overlapping start2
        max_tries = 10
        start1 = None
        start2 = None
        for _ in range(max_tries):
            s1 = random.uniform(0, total_duration - dur1)
            e1 = s1 + dur1

            # Allowed ranges for start2 (inclusive endpoints allow adjacency)
            candidates = []
            if s1 - dur2 >= 0:
                candidates.append((0.0, s1 - dur2))  # place segment 2 before seg1
            if (total_duration - dur2) >= e1:
                candidates.append((e1, total_duration - dur2))  # place seg2 after seg1

            if candidates:
                region = random.choice(candidates)
                s2 = random.uniform(region[0], region[1])
                start1, start2 = s1, s2
                break

        # 5) Fallback: if we couldn't find placement by random sampling,
        # place both segments adjacent at a random location (guaranteed to fit)
        if start1 is None:
            # pick a random start position for the two-adjacent-blocks
            free_space = total_duration - (dur1 + dur2)
            # free_space >= 0 due to our duration sampling logic
            s = random.uniform(0.0, free_space)
            if random.random() < 0.5:
                start1 = s
                start2 = s + dur1
            else:
                start2 = s
                start1 = s + dur2

        # 6) Load both segments (librosa.load uses seconds for offset & duration)
        with suppress_stderr():
            seg1, _ = librosa.load(audio_path, sr=self.sr, offset=float(start1), duration=float(dur1))
            seg2, _ = librosa.load(audio_path, sr=self.sr, offset=float(start2), duration=float(dur2))

        return seg1, seg2

    def return_audio_pair(self, item):
        """Return two non-overlapping audio segments from the same file"""
        if 'audio_path' in item.keys():
            audio_path = item['audio_path']
            seg1, seg2 = self.read_audio(audio_path)
            return seg1, seg2
        else:
            raise ValueError("Item must contain 'audio_path' key.")

    def __getitem__(self, idx):
        item = self.data[idx]
        try:
            seg1, seg2 = self.return_audio_pair(item)
        except Exception as e:
            print(f"Error processing item at index {idx}: {item}")
            print(f"Exception: {e}")
            raise e

        return {
            "audio_1": torch.tensor(seg1.copy(), dtype=torch.float32),
            "audio_2": torch.tensor(seg2.copy(), dtype=torch.float32),
        }


def collate_fn(batch):
    audio_1 = [b["audio_1"] for b in batch] # (B, T)
    audio_2 = [b["audio_2"] for b in batch] # (B, T)
    # Pad sequences to the max length in the batch
    padded_a1_wavs = torch.nn.utils.rnn.pad_sequence(audio_1, batch_first=True) # (B, T_max)
    padded_a2_wavs = torch.nn.utils.rnn.pad_sequence(audio_2, batch_first=True) # (B, T_max)
    return {"audio_1": padded_a1_wavs, "audio_2": padded_a2_wavs}

# -----------------------
# Main training
# -----------------------
def main(files: dict):
    rank, local_rank, world_size = setup_distributed()
    device = torch.device(f"cuda:{local_rank}")

    if rank == 0:
        print(f"Rank {rank}: loading processor and base model...")
    
    # Dataset + Samplers
    train_dataset = AudioTextDataset(files['train'], split="train")
    train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset, num_replicas=world_size, rank=rank, shuffle=True)
    train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, sampler=train_sampler,
                              collate_fn=lambda b: collate_fn(b),
                              num_workers=NUM_WORKERS, pin_memory=True)

    val_dataset = AudioTextDataset(files['validation'], split="validation")
    val_sampler = torch.utils.data.distributed.DistributedSampler(val_dataset, num_replicas=world_size, rank=rank, shuffle=False)
    val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE, sampler=val_sampler,
                            collate_fn=lambda b: collate_fn(b),
                            num_workers=NUM_WORKERS, pin_memory=True)


    # Base model
    config = StructureDerivationModelConfig()
    model = StructureDerivationModel(config)
    model = model.to(device)
    print(f"Rank {rank}: Model Initialized.")

    model = DDP(
        model,
        device_ids=[local_rank],
        output_device=local_rank,
        find_unused_parameters=True
    )
    print(f"Rank {rank}: DDP setup complete.")

    # Debug print
    trainable_count = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"Trainable params: {trainable_count:,}")

    trainable_params = [p for p in model.parameters() if p.requires_grad]
    optimizer = AdamW(trainable_params, lr=LR)

    num_update_steps_per_epoch = len(train_loader) # Already accounts for DDP
    max_train_steps = int((NUM_EPOCHS * num_update_steps_per_epoch) / GRADIENT_ACCUMULATION_STEPS)
    num_warmup_steps = int(0.01 * max_train_steps)
    if rank == 0:
        print(f"Rank {rank}: max_train_steps={max_train_steps}, num_warmup_steps={num_warmup_steps}")
    # Scheduler: linear warmup then decay
    lr_scheduler = get_scheduler(
        name="cosine",              # "linear", "cosine", "cosine_with_restarts", etc.
        optimizer=optimizer,
        num_warmup_steps=num_warmup_steps,
        num_training_steps=max_train_steps,
    )

    # Load checkpoint if available
    if LOAD_FROM_CHECKPOINT and rank == 0:
        ckpt = torch.load(os.path.join(CHECKPOINTS_DIR, "checkpoint.pt"), map_location=device)
        model.module.load_state_dict(ckpt["model"])  # `.module` because of DDP
        optimizer.load_state_dict(ckpt["optim"])

    # TensorBoard writer (rank 0 only)
    if rank == 0 and USE_TENSORBOARD:
        os.makedirs(TENSORBOARD_LOG_DIR, exist_ok=True)
        tb_writer = SummaryWriter(log_dir=TENSORBOARD_LOG_DIR)
    else:
        tb_writer = None

    # ---- Resume from metrics.json if available ----
    start_epoch = 0
    if LOAD_FROM_CHECKPOINT:
        metrics_path = os.path.join(CHECKPOINTS_DIR, "training_metrics.json")
        if os.path.exists(metrics_path):
            with open(metrics_path, "r") as f:
                try:
                    metrics_log = json.load(f)
                    if isinstance(metrics_log, list) and metrics_log:
                        last_entry = metrics_log[-1]
                        start_epoch = last_entry.get("epoch", 0)
                        best_val_loss = last_entry.get("best_val_loss", float("inf"))
                        # best_val_loss = float("inf")
                        ema_loss = last_entry.get("ema_train_loss", None)
                        if rank == 0:
                            print(f"Resuming from epoch {start_epoch+1} with best_val_loss={best_val_loss:.4f} and ema_loss={ema_loss:.4f}")
                    else:
                        metrics_log = []
                except json.JSONDecodeError:
                    metrics_log = []
        else:
            metrics_log = []
    else:
        metrics_log = []
        best_val_loss = float('inf')
        ema_loss = None

    ema_beta = 0.98  # smoothing factor
    optimizer.zero_grad(set_to_none=True)
    scaler = torch.amp.GradScaler()

    for epoch in range(start_epoch, NUM_EPOCHS):
        train_sampler.set_epoch(epoch)
        model.train()
        train_dataset.on_epoch_end()

        train_loss_sum = 0

        train_loader_tqdm = tqdm(train_loader, desc=f"Epoch {epoch+1} Training", disable=(rank != 0), 
                                 leave=False, position=0, dynamic_ncols=True)
        for step, inputs in enumerate(train_loader_tqdm):
            audio_1 = inputs["audio_1"].to(device)  # (B, T)
            audio_2 = inputs["audio_2"].to(device)  # (B, T)

            outputs = model(audio_1, audio_2, infer_mode=False)
            loss = outputs["loss"]

            train_loss_sum += loss.item() * audio_1.size(0)
            loss_val = loss.item()
            ema_loss = loss_val if ema_loss is None else (ema_beta * ema_loss + (1 - ema_beta) * loss_val)
            
            torch.autograd.set_detect_anomaly(True)
            scaler.scale(loss).backward()

            if (step + 1) % GRADIENT_ACCUMULATION_STEPS == 0 or (step + 1) == len(train_loader):
                scaler.unscale_(optimizer) # Unscale gradients before clipping
                torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                scaler.step(optimizer)
                scaler.update()
                lr_scheduler.step()
                optimizer.zero_grad(set_to_none=True)

            if step % LOG_STEP == 0 and rank == 0:
                train_loader_tqdm.set_postfix(loss=f"{loss_val:.4f}", ema_loss=f"{ema_loss:.4f}")

                # Add TensorBoard logging
                if USE_TENSORBOARD:
                    global_step = epoch * len(train_loader) + step
                    tb_writer.add_scalar("Train/StepLoss", loss_val, global_step)
                    tb_writer.add_scalar("Train/StepEMA", ema_loss, global_step)
                    current_lr = optimizer.param_groups[0]["lr"]
                    tb_writer.add_scalar("Train/LearningRate", current_lr, global_step)

            del inputs
            torch.cuda.empty_cache()

        # ---- Validation ----
        model.eval()
        val_loss_sum = 0

        val_loader_tqdm = tqdm(val_loader, desc=f"Epoch {epoch+1} Validation", disable=(rank != 0), 
                                 leave=False, position=0, dynamic_ncols=True)
        with torch.no_grad():
            for inputs in val_loader_tqdm:
                audio_1 = inputs["audio_1"].to(device)  # (B, T)
                audio_2 = inputs["audio_2"].to(device)  # (B, T)

                outputs = model(audio_1, audio_2, infer_mode=True)
                loss = outputs["loss"]
                    
                val_loss_sum += loss.item() * audio_1.size(0)

                del inputs
                torch.cuda.empty_cache()

        # ---- Reduce metrics across ranks ----
        val_metrics_t = torch.tensor([val_loss_sum, len(val_loader.dataset)], device=device) 
        dist.all_reduce(val_metrics_t, op=dist.ReduceOp.SUM)

        avg_val_loss_global = val_metrics_t[0].item() / val_metrics_t[1].item()

        # ---- Save checkpoint & log JSON (rank 0 only) ----
        if rank == 0:
            print(f"[Epoch {epoch+1}] EMA Train Loss: {ema_loss:.4f}, Val Loss: {avg_val_loss_global:.4f}")
            
            if USE_TENSORBOARD:
                tb_writer.add_scalar("Train/EpochEMA", ema_loss, epoch+1)
                tb_writer.add_scalar("Val/EpochLoss", avg_val_loss_global, epoch+1)

        should_save = avg_val_loss_global < best_val_loss
        best_val_loss = min(best_val_loss, avg_val_loss_global)

        if should_save and rank == 0:
            print(f"Best validation loss improved to {best_val_loss:.4f}, saving checkpoint...")
            os.makedirs(CHECKPOINTS_DIR, exist_ok=True)
            torch.save(
                {"model": model.module.state_dict(), "optim": optimizer.state_dict()},
                os.path.join(CHECKPOINTS_DIR, "checkpoint.pt")
            )

        if rank == 0:
            metrics_path = os.path.join(CHECKPOINTS_DIR, "training_metrics.json")
            if os.path.exists(metrics_path) and epoch > 0:
                try:
                    with open(metrics_path, "r") as f:
                        existing = json.load(f)
                        if not isinstance(existing, list):
                            existing = []
                except json.JSONDecodeError:
                    existing = []
            else:
                existing = []
            existing.append({
                "epoch": epoch + 1,
                "ema_train_loss": ema_loss,
                "val_loss": avg_val_loss_global,
                "best_val_loss": best_val_loss
            })
            with open(metrics_path, "w") as f:
                json.dump(existing, f, indent=2)


        # Free memory
        torch.cuda.empty_cache()

    if tb_writer is not None and USE_TENSORBOARD:
        tb_writer.close()


if __name__ == "__main__":
    # Read all jsonl files in the DATA_DIRS
    # train_files, validation_files = create_reproducible_splits(DATA_DIRS[0], seed=42)
    train_files = read_jsonl_files(DATA_DIRS, split="train")
    validation_files = read_jsonl_files(DATA_DIRS, split="validation")
    # test_files = read_jsonl_files(DATA_DIRS, split="test")
    if DEBUG:
        USE_TENSORBOARD = False
        # For debugging, limit the number of training files
        train_files = train_files[:10000]
        validation_files = validation_files[:100]

    main(files = {'train': train_files, 'validation': validation_files})
