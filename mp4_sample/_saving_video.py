# -*- coding: utf-8 -*-

import numpy as np
import cv2

fps = 15
size = (640,480)

cap = cv2.VideoCapture(0)
cap.set(3, size[0])  # Width
cap.set(4, size[1])  # Heigh
cap.set(5, fps)   # FPS

fourcc = cv2.VideoWriter_fourcc(*'DIB ')
# out = cv2.VideoWriter('output.avi',fourcc, fps, size)
out = cv2.VideoWriter('output.mp4',fourcc, fps, size)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release
cap.release()
out.release()
cv2.destroyAllWindows()
