# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/igo.jpg"
else:
    image_path = str(args[1])


#-----------------------------------------------------------------------------


from matplotlib import pyplot as plt
from matplotlib import image as image

I = image.imread(image_path)
G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# Canny Edge Detection:
Threshold1 = 150;
Threshold2 = 350;
FilterSize = 5
E = cv2.Canny(G, Threshold1, Threshold2, FilterSize)

Rres = 1
Thetares = 1*np.pi/180
Threshold = 100
minLineLength = 1
maxLineGap = 10
lines = cv2.HoughLinesP(E,Rres,Thetares,Threshold,minLineLength,maxLineGap)
N = lines.shape[0]
print(len(lines))
for i in range(N):
    x1 = lines[i][0][0]
    y1 = lines[i][0][1]
    x2 = lines[i][0][2]
    y2 = lines[i][0][3]
    cv2.line(I,(x1,y1),(x2,y2),(255,0,0),2)

while True:
    cv2.imshow("data",I)
    a = cv2.waitKey(10)
    if a>0:
        if a == 27:
            break

# while True:
#     plt.figure(),plt.imshow(I),plt.title('Hough Lines'),plt.axis('off')
#     plt.show()
#     if a>0:
#         if a == 27:
#             break











