# -*- coding: utf-8 -*-
import sys
import cv2
import numpy as np

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/520f8a8d.jpg"
else:
    image_path = str(args[1])

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 100)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/180,50)
# lines = cv2.HoughLines(edges,1,np.pi/180,15)
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 100*(-b))
    y1 = int(y0 + 100*(a))
    x2 = int(x0 - 100*(-b))
    y2 = int(y0 - 100*(a))

    cv2.line(img,(x1,y1),(x2,y2),(255,255,255),2)

# cv2.imwrite('hoge.jpg',img)
while True:
	cv2.imshow("data",img)
	a = cv2.waitKey(10)
	if a>0:
		if a == 27:
			break
