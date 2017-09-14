# -*- coding: utf-8 -*-
import os
import cv2
import glob
import numpy as np
from PIL import Image, ImageTk
#ubuntu:
#sudo apt-get install python-imaging-tk

for name in glob.glob("folder path here /*.jpg"):
    print(name)

    img = Image.open(name)
    os.remove(name)
    img.save(name.replace(".jpg", ".png"))





