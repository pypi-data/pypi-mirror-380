import os
import json
import torch
import torch.distributed as dist

# -----------------------
# Distributed helpers
# -----------------------
def setup_distributed():
    """
    Expects torchrun / torch.distributed to set RANK, WORLD_SIZE, LOCAL_RANK, etc.
    """
    if "RANK" in os.environ and "WORLD_SIZE" in os.environ:
        rank = int(os.environ["RANK"])
        world_size = int(os.environ["WORLD_SIZE"])
        local_rank = int(os.environ.get("LOCAL_RANK", rank % torch.cuda.device_count()))
    else:
        # Fallback single-process
        rank = 0
        local_rank = int(os.environ.get("LOCAL_RANK", 0))
        world_size = 1

    # Set device for this process
    torch.cuda.set_device(local_rank)
    dist.init_process_group(backend="nccl", init_method="env://")
    return rank, local_rank, world_size


def cleanup():
    dist.destroy_process_group()

def read_jsonl_files(data_dirs, split="train"):
    """
    Reads all jsonl files in the specified directories and returns a list of dictionaries.
    """
    files = []
    for file in data_dirs:
        if os.path.exists(file):
            with open(file, 'r') as f:
                for line in f:
                    # Parse the JSON string into a dictionary
                    data = json.loads(line.strip())
                    # Now you can access the dictionary keys
                    if data["split"] == split:
                        files.append(data)
        else:
            print(f"Warning: {file} does not exist. Skipping.")
    return files