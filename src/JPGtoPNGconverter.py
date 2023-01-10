import os, sys, pathlib
from PIL import Image


image_folder_path = sys.argv[1]
result_folder_path = sys.argv[2]

from os import listdir
from os.path import isfile, join


jpg_files = [
    f
    for f in os.listdir(image_folder_path)
    if pathlib.Path(join(image_folder_path, f)).suffix == ".jpg"
]
for image_name in jpg_files:
    img = Image.open(join(image_folder_path, image_name))
    new_image_name = pathlib.Path(image_name).stem + ".png"
    img.save(join(result_folder_path, new_image_name), "png")
