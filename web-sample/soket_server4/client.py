import cv2
import numpy as np
import socket
import sys
# import pickle
import cPickle as pickle
import struct ### new code
import time

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))
while True:
    ret,frame=cap.read()
    print(type(frame))
    #TODO:サイズを落としたい。
    # size = (826,1169)
    # img = cv2.resize(img, size)

    data = pickle.dumps(frame) ### new code
    clientsocket.sendall(struct.pack("L", len(data))+data) ### new code
    time.sleep(1)

