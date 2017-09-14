# -*- coding: utf-8 -*-

#python2

from flask import Flask, render_template, Response
#from camera import VideoCamera
from time import time
from PIL import Image
import cv2
import numpy as np

class Camera(object):
    def __init__(self, cap):
        rc,img = cap.read()

    def get_frame(self):
        self.frames = open("stream.jpg", 'w+')
        s, img = cap.read()
        if s:   # frame captures without errors...
            cv2.imwrite("stream.jpg", img)  # Save image...
        return self.frames.read()


cap=cv2.VideoCapture(0)
imagen = cap.read()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera(cap)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=False)

 