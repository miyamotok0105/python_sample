# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np

in_dir_path = ""
out_dir_path = ""
# size = (512,512)
size = (1169,826)

try:
    img = cv2.imread("S__24879120.jpg")
    height, width = img.shape[:2]
    img = cv2.resize(img, size)
    cv2.imwrite("S__24879120_mid.jpg", img)
    # cv2.imwrite(name, img)
    # while True:
    #     cv2.imshow("data",img)
    #     a = cv2.waitKey(10)
    #     if a>0:
    #         if a == 27:
    #             break

except Exception as e:
    print("exception args:", e.args)
    fuga()




