# -*- coding: utf-8 -*-
import sys
import cv2
import math
import numpy as np

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/520f8a8d.jpg"
else:
    image_path = str(args[1])

img = cv2.imread(image_path)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst = cv2.Canny(gray, 1100, 200)

# while True:
#   cv2.imshow("data",dst)
#   a = cv2.waitKey(10)
#   if a>0:
#       if a == 27:
#           break



lines= cv2.HoughLines(dst, 100, math.pi/180.0, 200, np.array([]), 0, 0)

line_len = 1000
a,b,c = lines.shape
print(len(lines))
for i in range(a):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0, y0 = a*rho, b*rho
    pt1 = ( int(x0+line_len*(-b)), int(y0+line_len*(a)) )
    pt2 = ( int(x0-line_len*(-b)), int(y0-line_len*(a)) )
    cv2.line(img, pt1, pt2, (0, 0, 0), 2, cv2.LINE_AA)


while True:
  cv2.imshow("data",img)
  a = cv2.waitKey(10)
  if a>0:
      if a == 27:
          break




