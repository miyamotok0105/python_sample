# -*- coding: utf-8 -*-
#python2

from flask import Flask, render_template, Response
#from camera import VideoCamera
# from time import time
from PIL import Image
import cv2
import os
import numpy as np
from soket_server import SoketServer
import threading
import time
import datetime

# soket_server = SoketServer()
# t = threading.Thread(target=soket_server.connect())
# t.start()


class Camera(object):
    def __init__(self):
        self.frames = []
        print(len(self.frames))

    def get_frame(self):
        now = datetime.datetime.now()
        
        img_arr = []
        for i in range(10):
            # if os.path.exists(os.path.join("img", "capture_{0:%Y%m%d-%H%M%S%f}.jpg".format(now - datetime.timedelta(milliseconds=int("%s"%(i)))))):
            #     img_arr.append(os.path.join("img", "capture_{0:%Y%m%d-%H%M%S%f}.jpg".format(now - datetime.timedelta(milliseconds=int("%s"%(i))))))
            #     break
            if os.path.exists(os.path.join("img", "capture_{0:%Y%m%d-%H%M%S}.jpg".format(now - datetime.timedelta(milliseconds=int("%s"%(i)))))):
                img_arr.append(os.path.join("img", "capture_{0:%Y%m%d-%H%M%S}.jpg".format(now - datetime.timedelta(milliseconds=int("%s"%(i))))))
        
        print("img_arr ", len(img_arr))
        self.frames = [open(str(f) , 'rb').read() for f in img_arr]
        time.sleep(1)
        # print(len(self.frames))
        return self.frames[0]

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def gen(camera):
    while True:
        try:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except:
            print("continue")
            continue

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)




