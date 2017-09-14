# -*- coding: utf-8 -*-
import cv2
import sys
import glob
import numpy as np

image_path = "1.png"

for name in glob.glob(image_path):
	print name
	img = cv2.imread(name, 1)
	height = img.shape[0]
	width = img.shape[1]
	x = 0  #cols
	y = 0  #rows
	# width = 833
	# height = 698

	dst = img[1159:y+height, x:x+width]
	cv2.imwrite("2.png", dst)










