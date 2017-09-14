#!/bin/env python
 
from flask import Flask, abort, render_template, request, url_for
from werkzeug import secure_filename
import cv2, numpy as np
 
application = Flask(__name__)
application.debug = True
 
## サービストップ
@application.route('/')
def index():
    return render_template('index.html')
 
## Cannyエッジ検出
@application.route('/cannyedge/<image>')
def canny(image=None):
    src = cv2.imread('./uploads/' + image)
    ## apply Canny Edge Detector
    ...
    return content
 
## Starキーポイント検出
@application.route('/starkeypoints/<image>')
def star(image=None):
    src = cv2.imread('./uploads/' + image)
    ## get Star Keypoints
    ...
    return content
 
## SURF特徴抽出
@application.route('/surf/<image>')
def surf(image=None):
    src = cv2.imread('./uploads/' + image)
    ## extract SURF
    ...
    return content
 
## 画像ファイルのアップロード
@application.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save('./uploads/' + secure_filename(f.filename))
    ...
 
## エラーハンドラ
@application.errorhandler(404)
def notfound(error):
    return 'not found', 404
 
if __name__ == '__main__':
    app.run()


