
#  /Volumes/Expansion/Raw_Footage

import os
import hashlib
from collections import defaultdict

filepath1 = "/Volumes/Expansion/testfolder"

def file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicate_files(directory):
    duplicates = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                file_checksum = file_hash(file_path)
                print(file)
                duplicates[file_checksum].append(file_path)
    return {k: v for k, v in duplicates.items() if len(v) > 1}


directory = filepath1 # <= add the path to your files here
duplicate_files = find_duplicate_files(directory)

if duplicate_files:
    print("duplicate files found:")
    for hash_value, files in duplicate_files.items():
        print(f"hash: {hash_value}")
        for file_path in files:
            print(f"- {file_path}")
else:
    print("no duplicate files found")
