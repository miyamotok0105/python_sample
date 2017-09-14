# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np


in_dir_path = ""
out_dir_path = ""
size = (826,1169)

dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test/*.png")

for name in glob.glob(dir_path):
    print(name)

    try:
        img = cv2.imread(name)
        height, width = img.shape[:2]
        img = cv2.resize(img, size)
        cv2.imwrite(name, img)
    except Exception as e:
        print("exception args:", e.args)
        fuga()

