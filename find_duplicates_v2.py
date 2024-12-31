import os
from pathlib import Path
# from PIL import Image, ImageStat

image_folder = r'/Volumes/Expansion/Raw_Footage'
image_path = Path(image_folder)

# image_files = [_ for _ in os.listdir(image_folder) if _.endswith('MP4')]
# print(len(image_files))
# adding some text for git practice

files = list(image_path.rglob("*.MP4*"))
# print(len(files))
# print(files[1])
# print(files[-1])
print(dir(files[1]))

