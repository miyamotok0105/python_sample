# -*- coding: utf-8 -*-
import os
import cv2
import sys
import numpy as np
from PIL import Image

path_jpg = "img/shougi.jpg"
path_png = "img/shougi.png"
image = np.asarray(Image.open(path_jpg))
print(image.shape)
