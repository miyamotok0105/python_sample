# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np


# args = sys.argv
in_dir_path = ""
out_dir_path = ""

img_path = "file path here"
img1_path = "hoge.png"
img2_path = "hoge2.png"

try:
    img1 = cv2.imread(img_path + img1_path)
    img2 = cv2.imread(img_path + img2_path)

    img4 = cv2.hconcat([img1, img2]) # 横方向の連結
    cv2.imwrite(img_path + "hconcat.png" , img4)

    # while True:
    #     cv2.imshow("data",img)
    #     a = cv2.waitKey(10)
    #     if a>0:
    #         if a == 27:
    #             break

except Exception as e:
    print("exception args:", e.args)
    fuga()

