# -*- coding: utf-8 -*-
import os
import sys
import cv2
import glob
import numpy as np
# args = sys.argv
in_dir_path = ""
out_dir_path = ""
# size = (512,512)
# if len(args) < 5:
#     in_dir_path = "img/520f8a8d.jpg"
#     out_dir_path = "img/resize_520f8a8d.jpg"
# else:
#     in_dir_path = str(args[1])
#     out_dir_path = str(args[2])
#     size = (int(args[3]),int(args[4]))

in_dir_path = "img/520f8a8d.jpg"
img1_path = "vconcat.png"
img2_path = "2.png"

try:
    img1 = cv2.imread(img_path + img1_path)
    img2 = cv2.imread(img_path + img2_path)

    img4 = cv2.vconcat([img1, img2]) 
    cv2.imwrite(img_path + "vconcat.png" , img4)

    # while True:
    #     cv2.imshow("data",img)
    #     a = cv2.waitKey(10)
    #     if a>0:
    #         if a == 27:
    #             break

except Exception as e:
    print("exception args:", e.args)
    # fuga()

