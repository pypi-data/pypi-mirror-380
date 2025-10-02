# import json
# import os
# import glob
# import librosa
# import tqdm

# # Get all *.jsonl files in the directory
# DATA_DIRS = glob.glob(os.path.join("/keshav/music_reward_project/music_reward/data/final_data_margin", '*.jsonl'))
# data_to_exclude = ["nsynth_captions", "fma_captions", "jazznet_captions"]
# DATA_DIRS = [d for d in DATA_DIRS if not any(excl in d for excl in data_to_exclude)]
# print(f"Found {len(DATA_DIRS)} JSONL files: {DATA_DIRS}")
# # Initialize tqdm for progress tracking
# progress_bar = tqdm.tqdm(total=len(DATA_DIRS), desc="Processing files")

# # Open the output file for writing
# output_file = os.path.join("/keshav/musical_structure_metrics/structure_derivation/data", "data.jsonl")
# with open(output_file, 'w') as f:
#     for file_path in DATA_DIRS:
#         with open(file_path, 'r') as file:
#             len_file = len(file.readlines())
#             for line in tqdm.tqdm(open(file_path, 'r'), total=len_file, desc=f"Processing {os.path.basename(file_path)}"):
#                 data = json.loads(line)
#                 if 'filepath' in data:
#                     audio_path = data['filepath']
#                 elif 'audio_filepath' in data:
#                     audio_path = data['audio_filepath']
#                 split = data.get('split')
#                 entry = {
#                     'audio_path': audio_path,
#                     'split': split
#                 }
#                 if audio_path and split:
#                     try:
#                         duration = librosa.get_duration(filename=audio_path)
#                         if duration >= 30:
#                             f.write(json.dumps(entry) + '\n')
#                     except Exception as e:
#                         print(f"Error processing file {audio_path}: {e}")
#         progress_bar.update(1)

# progress_bar.close()


import json
import os
import glob
import librosa
import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Get all *.jsonl files in the directory
DATA_DIRS = glob.glob(os.path.join("/keshav/music_reward_project/music_reward/data/final_data_margin", '*.jsonl'))
data_to_exclude = ["nsynth_captions", "fma_captions", "jazznet_captions"]
DATA_DIRS = [d for d in DATA_DIRS if not any(excl in d for excl in data_to_exclude)]
print(f"Found {len(DATA_DIRS)} JSONL files: {DATA_DIRS}")

output_file = os.path.join("/keshav/musical_structure_metrics/structure_derivation/data", "data_longer.jsonl")

# Worker function to process one JSON line
def process_line(line):
    try:
        data = json.loads(line)
        audio_path = data.get('filepath') or data.get('audio_filepath')
        split = data.get('split')
        if audio_path and split:
            duration = librosa.get_duration(filename=audio_path)
            if duration > 60:
                return {'audio_path': audio_path, 'split': split}
    except Exception as e:
        print(f"Error processing line: {e}")
    return None

# Threaded execution
with open(output_file, 'w') as f_out:
    for file_path in DATA_DIRS:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        results = []
        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            futures = [executor.submit(process_line, line) for line in lines]
            for future in tqdm.tqdm(as_completed(futures), total=len(lines), desc=f"Processing {os.path.basename(file_path)}"):
                res = future.result()
                if res:
                    f_out.write(json.dumps(res) + "\n")
