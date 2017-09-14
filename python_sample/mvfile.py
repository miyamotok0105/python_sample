# -*- coding: utf-8 -*-
#ファイルを移動する
import os
import sys
import cv2
import glob
import shutil
import numpy as np

base_folder = "hogehoge"


for root, dirs, files in os.walk(base_folder):
	xmls = filter(lambda f: f.endswith(".jpg"), files)
	for xml in xmls:
		print(os.path.join(root, xml))
		shutil.move(os.path.join(root, xml), os.path.join(base_folder, xml))



