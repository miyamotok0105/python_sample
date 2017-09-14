# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np

in_dir_path = ""
out_dir_path = ""
size = (826,1169)
in_dir_path = "dog1.png"

try:
    img = cv2.imread(in_dir_path)
    height, width = img.shape[:2]
    img = cv2.resize(img, size)
    cv2.imwrite(in_dir_path, img)

except Exception as e:
    print("exception args:", e.args)






