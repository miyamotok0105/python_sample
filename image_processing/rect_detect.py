# -*- coding: utf-8 -*-
import cv2
import sys
import numpy as np

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/520f8a8d.jpg"
else:
    image_path = str(args[1])

img = cv2.imread(image_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 100)
cv2.imwrite('img/rect_detect_edged.jpg', edged)
_, rect_contours, _= cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
rect_and_contours = np.copy(img)

min_rect_area = 60
large_contours = [cnt for cnt in rect_contours if cv2.contourArea(cnt) > min_rect_area]
cv2.drawContours(rect_and_contours, large_contours, -1, (255,0,0))
print('number of img: %d' % len(large_contours))
bounding_img = np.copy(img)
 
for i, contour in enumerate(large_contours):
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(bounding_img, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imwrite('img/rect_detect.jpg', bounding_img)
    dst = img[y:y+h, x:x+w]
    cv2.imwrite('img/rect_detect_%s.jpg' %(i), dst)

cv2.imwrite('img/rect_detect.jpg', bounding_img)




