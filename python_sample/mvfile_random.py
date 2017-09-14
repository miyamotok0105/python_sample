# -*- coding: utf-8 -*-
#ランダムにファイルを移動する
import os
import sys
import cv2
import glob
import random
import shutil
import numpy as np

base_folder = "hogehoge"
to_folder = "hogehoge"

files = os.listdir(base_folder)

for file in random.sample(files, 4000):
    print(file)
    shutil.move(os.path.join(base_folder, file), to_folder)




