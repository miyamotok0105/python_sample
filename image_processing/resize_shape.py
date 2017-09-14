# -*- coding: utf-8 -*-
import os
import cv2
import sys
import numpy as np
from PIL import Image

path_png = "hoge.png"
path_jpg = "hoge2.jpg"

image = Image.open(path_png).convert('P')
image.save(path_png)
rgb_im = Image.open(path_png).convert('RGB')
rgb_im.save(path_jpg)

print(image)
print(rgb_im)
print(np.asarray(image).shape)
print(np.asarray(rgb_im).shape)

