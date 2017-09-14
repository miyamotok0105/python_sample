# -*- coding: utf-8 -*-
import numpy as np
import cv2


cap = cv2.VideoCapture('load_min1_5fps.mp4')
fps = 15
size = (640,480)
cap.set(3, size[0])  # Width
cap.set(4, size[1])  # Heigh
cap.set(5, fps)   # FPS

while(cap.isOpened()):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
