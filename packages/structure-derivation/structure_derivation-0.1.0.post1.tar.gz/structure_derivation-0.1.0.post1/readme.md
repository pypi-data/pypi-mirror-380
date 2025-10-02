---
license: apache-2.0
language:
- en
tags:
- music
- audio
- structure
---

# Structural Derivation: A Model & Metric for Musical Structure Analysis

This repository contains a model for learning structural embeddings of music by contrasting segments from the same song against segments from different songs. It can be used to generate two novel metrics for any given audio file: the **Structural Derivation Consistency (SDC)** score and the **Structural Diversity** score.

These metrics are particularly useful for quantifying the high-level thematic structural consistency and structural diversity of a musical piece. Together, these metrics provide a lens on both the cohesion and variation of a track’s structure, distinguishing human-composed music (typically higher consistency and balanced diversity) from AI-generated music (often lower consistency or uneven diversity due to thematic drifts).

---

## 🎵 Key Metrics

The model analyzes a song by first splitting it into segments (e.g., 10-20 seconds each) and generating a high-level embedding for each segment. These embeddings are then used to compute the following scores.

### 1. Structural Derivation Consistency (SDC) Score

The SDC score quantifies a song's **structural and thematic integrity**. It serves as a proxy for **musical narrative consistency**, measuring how well a song "remembers" and develops the musical ideas presented in its opening segment. In other words, it reflects how structurally coherent and thematically consistent the song is in embedding space.

* **How it works:** The score is the average cosine similarity between the embedding of the first segment (S1) and every subsequent segment (S2, S3, ..., SN).
* **Interpretation:**
    * A **high SDC score** suggests the piece is thematically consistent. Like a well-written story, it builds upon its initial premise. This is characteristic of human-composed music, which often uses repetition, variation, and development of a core motif or theme.
    * A **low SDC score** indicates potential **"thematic drift."** The song's later sections diverge significantly from its beginning, lacking a clear connection to the initial musical statement. This can be a trait of AI-generated music that struggles with long-form compositional structure.

### 2. Structural Diversity Score

The Structural Diversity score measures the **variety of distinct musical ideas** within a single piece of music. It complements the SDC score by providing insight into the song's complexity and repetitiveness. In other words, it reflects the variety and richness of internal structures by capturing how different the segments are from one another.

* **How it works:** The score is calculated using the [Vendi Score](https://github.com/verga11/vendi-score) on the similarity matrix derived from all segment embeddings.
* **Interpretation:**
    * A **high Diversity score** indicates that the song contains a wide range of different-sounding segments. The piece is musically rich and varied.
    * A **low Diversity score** suggests the song is repetitive or monotonous, with very similar-sounding segments throughout.

A compelling musical piece might exhibit both high SDC (it's coherent) and high Diversity (it's interesting and not overly repetitive).

---

## 💻 Installation & Usage

### 1. Installation

Install the package and its dependencies directly from the GitHub repository:

```bash
pip install structural-derivation
```

### 2. Example Usage

The following script loads the model from Hugging Face, processes a list of audio files, and prints the resulting scores. The `process_audio_files` function handles splitting the audio, batching, and computing both metrics.

```python
import torch
from structure_derivation.inference.batch_inference import process_audio_files
from structure_derivation.model.model import StructureDerivationModel

# 1. Set up the device and load the model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# The model will be automatically downloaded from Hugging Face
model = StructureDerivationModel.from_pretrained(
    "keshavbhandari/structure-derivation"
)
model.to(device)
model.eval()

# 2. Define the list of audio files you want to analyze
my_audio_files = [
    "path/to/your/song1.mp3",
    "path/to/your/song2.wav",
    "path/to/another/track.flac",
]

# 3. Analyze the files to get the scores
# This function returns a dictionary with file paths as keys
results = process_audio_files(audio_paths=my_audio_files, model=model, batch_size=128, segment_seconds=10, target_sr=32000)

# 4. Print the results
for path, res in results.items():
    print(f"\nResults for {path}:")
    print("Cosine similarities with S1:", res["similarities"])
    print("Average Structure Derivation:", res["avg_structure_derivation"])
    print("Vendi score:", res["vendi_score"])
```

### 3. Model Architecture & Training
Architecture
The core of this model is the Hierarchical Token-Semantic Audio Transformer (HTS-AT) encoder. This architecture, introduced by Chen et al., is a highly efficient and powerful audio transformer.

Key features of HTS-AT include:
- **Hierarchical Structure:** It uses Patch-Merge layers to gradually reduce the number of audio tokens as they pass through the network. This significantly reduces GPU memory consumption and training time compared to standard transformers.
- **Windowed Attention:** Instead of computing self-attention across the entire audio spectrogram, it uses a more efficient windowed attention mechanism from the Swin Transformer. This captures local relationships effectively while remaining computationally tractable.
- **High Performance:** HTS-AT achieves state-of-the-art results on major audio classification benchmarks like AudioSet and ESC-50.

This architecture is ideal for our purpose as it can efficiently process long audio clips and learn rich, meaningful representations of musical structure.

Training
The model was trained using a contrastive learning objective on a large-scale corpus of nearly 400,000 music files (each longer than one minute) for 20 epochs. The training data was sourced from a combination of the following publicly available datasets:

- GiantSteps Key Dataset

- FSL10K

- Emotify

- Emopia

- ACM MIRUM

- JamendoMaxCaps

- MTG-Jamendo

- SongEval

- Song Describer

- ISMIR04

- Hainsworth

- Saraga

- DEAM

- MAESTRO v3.0.0

### 4. Re-training on Custom Data
If you wish to re-train the model on your own dataset, you can use the provided training script. Run the following command from the root of the repository, adjusting the GPU devices as needed:

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5 torchrun --nproc_per_node=6 --master_port=12345 structure_derivation/train/train.py
```

This will start the training process using the default hyperparameters specified in the script. You can modify these parameters as needed to suit your dataset and training requirements.