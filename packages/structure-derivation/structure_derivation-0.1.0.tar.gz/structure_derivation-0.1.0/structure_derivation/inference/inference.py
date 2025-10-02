import librosa
import os
import numpy as np
import torch
import torch.nn.functional as F
from structure_derivation.model.model import StructureDerivationModel, StructureDerivationModelConfig
from vendi_score import vendi

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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

def split_audio(audio_path, segment_seconds=10, target_sr=32000):
    """Load audio and split into N non-overlapping segments of segment_seconds each."""
    audio, sr = librosa.load(audio_path, sr=target_sr, mono=True)
    segment_len = segment_seconds * target_sr
    total_len = len(audio)
    segments = []
    for start in range(0, total_len, segment_len):
        end = start + segment_len
        if end <= total_len:
            segments.append(audio[start:end])
    return segments, sr

def compute_embeddings(model, segments, device):
    """Pass each segment through the model to get latent_output embeddings."""
    embeddings = []
    for seg in segments:
        seg_tensor = torch.tensor(seg, dtype=torch.float32).unsqueeze(0).to(device)  # (1, T)
        with torch.no_grad():
            out = model(seg_tensor, infer_mode=True)
        embeddings.append(out["latent_output"])  # (1, D)
    return torch.cat(embeddings, dim=0)  # (N, D)

def compute_structure_derivation(embeddings):
    """Cosine similarity between first segment and all others."""
    ref = embeddings[0].unsqueeze(0)  # (1, D)
    sims = F.cosine_similarity(ref, embeddings[1:], dim=1)  # (N-1,)
    return sims.cpu().numpy()

def compute_vendi(embeddings):
    """Compute cosine similarity matrix between all embeddings."""
    norm_emb = F.normalize(embeddings, p=2, dim=1)  # (N, D)
    sim_matrix = torch.matmul(norm_emb, norm_emb.T)  # (N, N)
    sim_matrix = sim_matrix.cpu().numpy()
    vendi_score = vendi.score_K(sim_matrix)
    return vendi_score


# ----------------- Usage -----------------
CHECKPOINTS_DIR = "/keshav/musical_structure_metrics/structure_derivation/artifacts/structure_derivation_model/checkpoint/"
ckpt_path = os.path.join(CHECKPOINTS_DIR, "checkpoint.pt")

model = load_model(ckpt_path, device)

audio_path = '/mnt/data/marble/mtg_jamendo/mtg-jamendo-dataset/data/raw_30s_audio/99/6699.mp3'
segments, sr = split_audio(audio_path, segment_seconds=10, target_sr=32000)
print(f"Split into {len(segments)} segments.")

embeddings = compute_embeddings(model, segments, device)
print("Embeddings shape:", embeddings.shape)  # (N, D)

similarities = compute_structure_derivation(embeddings)
print("Cosine similarities with S1:", similarities)

# Average Structure Derivation score
avg_structure_derivation = similarities.mean()
print("Average Structure Derivation similarity with S1:", avg_structure_derivation)

# Vendi score
vendi_score = compute_vendi(embeddings)
print("Vendi score:", vendi_score)
