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


img = cv2.imread(image_path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,1,minLineLength,maxLineGap)

print(len(lines[0]))
for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# cv2.imwrite('houghlines5.jpg',img)

while True:
  cv2.imshow("data",img)
  a = cv2.waitKey(10)
  if a>0:
      if a == 27:
          break





