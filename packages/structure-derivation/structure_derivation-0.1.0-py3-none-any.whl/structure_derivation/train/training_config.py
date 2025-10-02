import os
import glob

# Configuration for the data
RAW_DATA_ROOT = "/data/shared/"
DATA_DIRS = glob.glob(os.path.join("/keshav/musical_structure_metrics/structure_derivation/data", '*.jsonl'))
datasets_to_include = ["data_longer.jsonl"]
DATA_DIRS = [d for d in DATA_DIRS if any(ds in os.path.basename(d) for ds in datasets_to_include)]

# Configuration for the training
MAX_AUDIO_LEN = 30                              # Maximum audio length in seconds
BATCH_SIZE = 32                                 # Batch size for training
NUM_WORKERS = 4                                 # Number of workers for data loading
LR = 1e-4                                       # Learning rate for the optimizer
NUM_EPOCHS = 20                                 # Number of epochs for training
GRADIENT_ACCUMULATION_STEPS = 1                 # Number of gradient accumulation steps
LOAD_FROM_CHECKPOINT = True                    # Whether to load weights from a checkpoint
USE_TENSORBOARD = True                          # Whether to use TensorBoard for logging
LOG_STEP = 5                                    # Step interval for logging training progress
DEBUG = False                                   # Whether to run in debug mode

LOGS_PATH = "structure_derivation/artifacts/structure_derivation_model/logs.txt"              # Path for logs
TENSORBOARD_LOG_DIR = "structure_derivation/artifacts/structure_derivation_model/tensorboard"  # Directory for TensorBoard logs
CHECKPOINTS_DIR = "structure_derivation/artifacts/structure_derivation_model/checkpoint"      # Directory for saving checkpoints