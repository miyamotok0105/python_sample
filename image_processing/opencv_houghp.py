# -*- coding: utf-8 -*-
import sys
import numpy as np
import cv2

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/520f8a8d.jpg"
else:
    image_path = str(args[1])


#-----------------------------------------------------------------------------
# img = cv2.imread(image_path)

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,200,400,apertureSize = 3)

# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
# print(len(lines))
# for x1,y1,x2,y2 in lines[0]:
#     print("done")
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


# # cv2.imwrite('hoge.jpg',img)
# # cv2.imwrite('canny.png',gray)
# while True:
# 	cv2.imshow("data",img)
# 	a = cv2.waitKey(10)
# 	if a>0:
# 		if a == 27:
# 			break

#-----------------------------------------------------------------------------


# img = cv2.imread(image_path)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 100
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,1,minLineLength,maxLineGap)

# print(len(lines[0]))
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# # cv2.imwrite('houghlines5.jpg',img)

# while True:
# 	cv2.imshow("data",img)
# 	a = cv2.waitKey(10)
# 	if a>0:
# 		if a == 27:
# 			break



#-----------------------------------------------------------------------------



# from matplotlib import pyplot as plt
# from matplotlib import image as image

# I = image.imread(image_path)
# G = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)

# # Canny Edge Detection:
# Threshold1 = 150;
# Threshold2 = 350;
# FilterSize = 5
# E = cv2.Canny(G, Threshold1, Threshold2, FilterSize)

# Rres = 1
# Thetares = 1*np.pi/180
# Threshold = 100
# minLineLength = 1
# maxLineGap = 200
# lines = cv2.HoughLinesP(E,Rres,Thetares,Threshold,minLineLength,maxLineGap)
# N = lines.shape[0]
# print(len(lines))
# for i in range(N):
#     x1 = lines[i][0][0]
#     y1 = lines[i][0][1]
#     x2 = lines[i][0][2]
#     y2 = lines[i][0][3]
#     cv2.line(I,(x1,y1),(x2,y2),(255,0,0),2)

# plt.figure(),plt.imshow(I),plt.title('Hough Lines'),plt.axis('off')
# plt.show()




#-----------------------------------------------------------------------------


# #http://stackoverflow.com/questions/30814018/how-do-i-get-houghlines-to-recognize-the-rest-of-the-lines-in-this-picture
# img = cv2.imread(image_path)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# threshhold, threshhold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# edges = cv2.Canny(threshhold_img, 150, 200, 3, 5)
# lines = cv2.HoughLinesP(edges,1,np.pi/180,100, minLineLength = 100, maxLineGap = 75)[0].tolist()

# # Vertical lines
# # lines = cv2.HoughLinesP(
# #     threshhold_img, 1, np.pi, threshold=100, minLineLength=100, maxLineGap=1)

# # Horizontal lines
# # lines2 = cv2.HoughLinesP(
# #     threshhold_img, 1, np.pi / 2, threshold=500, minLineLength=500, maxLineGap=1)


# for x1,y1,x2,y2 in lines:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

# # cv2.imwrite('hough4.jpg',img)
# while True:
# 	cv2.imshow("data",img)
# 	a = cv2.waitKey(10)
# 	if a>0:
# 		if a == 27:
# 			break


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
thresh = cv2.dilate(thresh,kernel,iterations = 10)
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
minArea=5000 #nothing
print len(contours)
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




