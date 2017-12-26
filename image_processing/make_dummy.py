# -*- coding: utf-8 -*-
import numpy as np
import cv2
image = np.zeros([480,640,3])
cv2.imwrite("image.jpg", image)

print(image.shape)
