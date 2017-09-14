# -*- coding: utf-8 -*-
#python2

from flask import Flask, render_template, Response
#from camera import VideoCamera
from time import time
from PIL import Image
import cv2
import numpy as np
from soket_server import SoketServer
import threading
import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import time
import datetime

# soket_server = SoketServer()
# t = threading.Thread(target=soket_server.connect())
# t.start()
# print("1")

class Camera(object):
	def __init__(self):
		# rc,img = cap.read()
		print("camera init")

	def get_frame(self):
		# self.frames = soket_server.frame
		# print(self.frames)
		self.frames = open("stream.jpg", 'w+')
		# s, img = cap.read()
		# if s:	# frame captures without errors...
		# 	cv2.imwrite("stream.jpg", img)	# Save image...
		return self.frames.read()

# cap=cv2.VideoCapture(0)
# imagen = cap.read()
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# def gen(camera):
# 	while True:
# 		# frame = camera.get_frame()
# 		frame = soket_server.connect()
# 		yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
def gen():

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
        frames = open("stream.jpg", 'w+')
        frame = frames.read()
        # print frame
        # now = datetime.datetime.now()
        # fmt_name = "stream.jpg".format(now)
        # cv2.imwrite(fmt_name, self.frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
# def video_feed():
#     return Response(gen(Camera()),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8082, debug=True, threaded=False)



