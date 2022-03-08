# Inspired by https://www.kaggle.com/odins0n/h-m-image-resizer-dataset-256x256

import cv2 
import os
import shutil

TARGET_SHAPE = (80,60)
INTERPOLATION = cv2.INTER_AREA
INPUT_DIR = "data/images/"
TARGET_DIR = "images_80_60/"

folders = os.listdir(INPUT_DIR)
for folder in folders:
    if folder == ".DS_Store":
        continue
    images = os.listdir(str(INPUT_DIR + folder))
    os.makedirs(str(TARGET_DIR  + folder) , exist_ok=True)
    for image in images:
        loaded_image = cv2.imread(str(INPUT_DIR + folder + "/" +  image))
        resized_image = cv2.resize(loaded_image, TARGET_SHAPE , interpolation =INTERPOLATION)
        cv2.imwrite(str(TARGET_DIR + folder + "/" +  image) , resized_image)
    print("FOLDER DONE - ", folder)
print("!CHECK! RESIZED IMAGE SHAPE - ",resized_image.shape)

print("DONE!!! ")