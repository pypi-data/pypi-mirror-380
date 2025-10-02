import librosa
import os
import numpy as np
import torch
import torch.nn.functional as F
from structure_derivation.model.model import StructureDerivationModel, StructureDerivationModelConfig
from vendi_score import vendi
from collections import defaultdict


# ----------------- Model Loader -----------------
def load_model(ckpt_path, device):
    config = StructureDerivationModelConfig()
    model = StructureDerivationModel(config)
    model.to(device)

    ckpt = torch.load(ckpt_path, map_location=device)
    if "module" in ckpt["model"]:
        model.module.load_state_dict(ckpt["model"]["module"])  # DDP checkpoint
    else:
        model.load_state_dict(ckpt["model"])
    model.eval()
    return model

def load_model_huggingface(device):
    model = StructureDerivationModel.from_pretrained(
    "keshavbhandari/structure-derivation"
    )
    model.to(device)
    model.eval()
    return model

# ----------------- Padding -----------------
def pad_segment(seg, target_len):
    """Pad 1D waveform to target_len with zeros."""
    if len(seg) < target_len:
        pad_width = target_len - len(seg)
        seg = np.pad(seg, (0, pad_width), mode="constant")
    return seg

# ----------------- Audio Split -----------------
def split_audio(audio_path, segment_seconds=10, target_sr=32000):
    audio, sr = librosa.load(audio_path, sr=target_sr, mono=True)
    segment_len = segment_seconds * target_sr
    total_len = len(audio)
    segments = []
    for start in range(0, total_len, segment_len):
        end = start + segment_len
        seg = audio[start:end]
        if len(seg) == segment_len:  # full segment
            segments.append(seg)
        elif len(seg) > 0:  # leftover shorter segment → pad
            seg = pad_segment(seg, segment_len)
            segments.append(seg)
    return segments, sr

# ----------------- Embeddings Batch -----------------
def compute_embeddings_batch(model, batch, device):
    """Compute embeddings for a batch of segments."""
    seg_tensors = torch.stack(
        [torch.tensor(seg, dtype=torch.float32) for seg in batch]
    ).to(device)  # (B, T)
    seg_tensors = torch.nn.utils.rnn.pad_sequence(seg_tensors, batch_first=True)  # pad if lengths differ
    seg_tensors = seg_tensors.to(device)

    with torch.no_grad():
        outputs = model(seg_tensors, infer_mode=True)

    return outputs["latent_output"]  # (B, D)


# ----------------- Scoring -----------------
def compute_structure_derivation(embeddings):
    """Cosine similarity between first segment and all others."""
    if embeddings.shape[0] <= 1:
        return np.array([]), float("nan")  # nothing to compare
    ref = embeddings[0].unsqueeze(0)  # (1, D)
    sims = F.cosine_similarity(ref, embeddings[1:], dim=1)  # (N-1,)
    return sims.cpu().numpy(), sims.mean().item()


def compute_vendi(embeddings):
    """Compute cosine similarity matrix between all embeddings."""
    norm_emb = F.normalize(embeddings, p=2, dim=1)  # (N, D)
    sim_matrix = torch.matmul(norm_emb, norm_emb.T)  # (N, N)
    sim_matrix = sim_matrix.cpu().numpy()
    vendi_score = vendi.score_K(sim_matrix)
    return vendi_score


# ----------------- Main Pipeline -----------------
def process_audio_files(audio_paths, model, batch_size=128, segment_seconds=10, target_sr=32000):
    """
    Processes a list of audio files:
      - Splits into segments
      - Runs batched inference
      - Computes Structure Derivation + Vendi per file
      - Keeps memory usage low
    """
    results = {}

    # Pre-split all audios into segments
    all_segments = []
    segment_map = []  # (audio_idx, segment_idx) for each segment
    for audio_idx, path in enumerate(audio_paths):
        segments, _ = split_audio(path, segment_seconds, target_sr)
        for seg_idx, seg in enumerate(segments):
            all_segments.append(seg)
            segment_map.append((audio_idx, seg_idx))

    # Group per audio so we know how many segments each has
    audio_segment_counts = defaultdict(int)
    for audio_idx, _ in segment_map:
        audio_segment_counts[audio_idx] += 1

    # Buffers for embeddings per audio
    audio_embeddings = defaultdict(list)

    # Process in batches
    for i in range(0, len(all_segments), batch_size):
        batch = all_segments[i : i + batch_size]
        batch_map = segment_map[i : i + batch_size]

        # Compute embeddings
        device = next(model.parameters()).device
        emb_batch = compute_embeddings_batch(model, batch, device)

        # Assign embeddings back to their audio
        for emb, (audio_idx, seg_idx) in zip(emb_batch, batch_map):
            audio_embeddings[audio_idx].append((seg_idx, emb.unsqueeze(0)))

        # Check if any audio file is complete → compute metrics & clear from memory
        completed_audios = []
        for audio_idx, segs in audio_embeddings.items():
            if len(segs) == audio_segment_counts[audio_idx]:
                # Sort segments by original order
                segs_sorted = [emb for _, emb in sorted(segs, key=lambda x: x[0])]
                embeddings = torch.cat(segs_sorted, dim=0)  # (N, D)

                # Compute metrics
                sims, avg_sim = compute_structure_derivation(embeddings)
                vendi_score = compute_vendi(embeddings)

                # Save results
                results[audio_paths[audio_idx]] = {
                    "similarities": sims,
                    "avg_structure_derivation": avg_sim,
                    "vendi_score": vendi_score,
                }

                # Mark for cleanup
                completed_audios.append(audio_idx)

        for audio_idx in completed_audios:
            del audio_embeddings[audio_idx]  # free memory

    return results


# ----------------- Usage -----------------

if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = StructureDerivationModel.from_pretrained(
    "keshavbhandari/structure-derivation"
    )
    model.to(device)
    model.eval()

    audio_paths = [
        "/mnt/data/marble/mtg_jamendo/mtg-jamendo-dataset/data/raw_30s_audio/91/1092591.mp3",
        "/mnt/data/marble/mtg_jamendo/mtg-jamendo-dataset/data/raw_30s_audio/93/1001893.mp3",
    ]

    results = process_audio_files(audio_paths, model, batch_size=128, segment_seconds=20, target_sr=32000)

    for path, res in results.items():
        print(f"\nResults for {path}:")
        print("Cosine similarities with S1:", res["similarities"])
        print("Average Structure Derivation:", res["avg_structure_derivation"])
        print("Vendi score:", res["vendi_score"])
