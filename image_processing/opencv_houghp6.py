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

##これは線がない場合
#http://stackoverflow.com/questions/39078999/how-to-recognize-text-regions-using-histogram
img = cv2.imread(image_path)

im_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)

edges = cv2.Canny(im_gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 100
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(thresh,(x1,y1),(x2,y2),(0),5)

kernel = np.ones((3,3),np.uint8)
thresh = cv2.dilate(thresh,kernel,iterations = 70)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
minArea=10000 #nothing
# print len(contours)
for cnt in contours:
    area=cv2.contourArea(cnt)
    if(area>minArea):
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img,[box],0,(0,0,255),2)

# cv2.imwrite('hough4.jpg',img)
while True:
	cv2.imshow("data",img)
	a = cv2.waitKey(10)
	if a>0:
		if a == 27:
			break






