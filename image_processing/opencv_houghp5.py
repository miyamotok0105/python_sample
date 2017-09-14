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


#http://stackoverflow.com/questions/30814018/how-do-i-get-houghlines-to-recognize-the-rest-of-the-lines-in-this-picture
img = cv2.imread(image_path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshhold, threshhold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
edges = cv2.Canny(threshhold_img, 100, 100, 3, 5)
lines = cv2.HoughLinesP(edges,1,np.pi/180,threshold=100, minLineLength = 10, maxLineGap = 110)[0].tolist()

# Vertical lines
# lines = cv2.HoughLinesP(
#     threshhold_img, 1, np.pi, threshold=100, minLineLength=100, maxLineGap=1)

# Horizontal lines
# lines2 = cv2.HoughLinesP(
#     threshhold_img, 1, np.pi / 2, threshold=500, minLineLength=500, maxLineGap=1)


for x1,y1,x2,y2 in lines:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

# cv2.imwrite('hough4.jpg',img)
while True:
	cv2.imshow("data",img)
	a = cv2.waitKey(10)
	if a>0:
		if a == 27:
			break







