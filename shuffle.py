import os
import random
import shutil

base_train = './fyp-data/train/straight'
base_test = './fyp-data/test/straight'
files = os.listdir(base_train)
images = []
for file in files:
    images.append(file)

random.shuffle(images)
print(images)
for i in range(int(len(images)*0.20)):
    shutil.move(base_train+'/'+images[i], base_test+'/'+images[i])
