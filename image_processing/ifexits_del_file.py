# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np

in_dir_path = ""
out_dir_path = ""

in_dir_path = "labels/*.txt"
diff_dir_path = "train/*.png"

for name in glob.glob(in_dir_path):
    file_name = os.path.basename(name)

    exists = False

    for name_diff in glob.glob(diff_dir_path):
        diff_file_name = os.path.basename(name_diff)
        if diff_file_name.replace(".png", "") == file_name.replace(".txt", ""):
            exists = True

    if exists == True:
        # print(file_name)
        a = ""
    else:
        print(name)
        try:
            os.remove(name)

        except Exception as e:
            print("exception args:", e.args)
            fuga()


    



