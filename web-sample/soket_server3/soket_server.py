import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import time
import datetime

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print 'Socket created'

s.bind((HOST,PORT))
print 'Socket bind complete'
s.listen(100)
print 'Socket now listening'

conn,addr=s.accept()

### new
data = ""
payload_size = struct.calcsize("L") 
print("payload_size " + str(payload_size))
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    ###

    frame=pickle.loads(frame_data)
    # print frame
    now = datetime.datetime.now()
    fmt_name = "capture_{0:%Y%m%d-%H%M%S}.jpg".format(now)
    cv2.imwrite(fmt_name, frame)

    time.sleep(1)
