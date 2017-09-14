# -*- coding:utf-8 -*-
#!/usr/bin/python
import socket 
import numpy  
import cv2  
import datetime

    
def getimage():
    #IPアドレスとポート番号は環境に応じて変更
    HOST = "153.120.159.78"
    PORT = 8000  
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((HOST,PORT))   
    sock.send('HELLO\n')  
    buf=''   
    recvlen=100
    while recvlen>0:  
        receivedstr=sock.recv(1024*8)  
        recvlen=len(receivedstr)  
        buf +=receivedstr  
    sock.close()  
    narray=numpy.fromstring(buf,dtype='uint8')  
    return cv2.imdecode(narray,1)  
  
while True:  
    img = getimage()

    now = datetime.datetime.now()
    fmt_name = "capture_{0:%Y%m%d-%H%M%S}.jpg".format(now)
    cv2.imshow(fmt_name, img)

