# -*- coding: utf-8 -*-
 #http://www.takunoko.com/blog/python%E3%81%A7%E9%81%8A%E3%82%93%E3%81%A7%E3%81%BF%E3%82%8B-part1-opencv%E3%81%A7%E9%A1%94%E8%AA%8D%E8%AD%98/
# 動画ファイルから、顔認識したものを取り出す 
# 分類器をアニメ向けのもの使用
import cv2
import time
 
# 分類器へのパス
cascade_path = "../haarcascades/haarcascade_fullbody.xml"
 
# 動画パス
video_path = "load_min1_5fps.mp4"
out_video_path = "load_min1_5fps_detect.mp4"
 
# colorはBGRの順番?
color = (0, 187, 254) #黄
#カスケード分類器の特徴量を取得する
cascade = cv2.CascadeClassifier(cascade_path)
 
# 動画のエンコード　とりあえず、これで動く拡張子はm4vで
# fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# 動画ファイル読み込み
cap = cv2.VideoCapture(video_path)
 
out = cv2.VideoWriter("face_output.m4v", fourcc, 30.0, (1280,720))
 
frame_num = 0
img_cnt = 0
# フレームごとの処理
while(cap.isOpened()):
  ret, frame = cap.read()
  if (ret == False):
    break
  frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))

  print("frame : %d" % frame_num)
  if len(facerect) > 0:
	#検出した顔を囲む矩形の作成
	for (x,y,w,h) in facerect:
		cv2.rectangle(frame, (x,y),(x+w,y+h), color, thickness=7)
		img_cnt += 1
		out.write(frame)
  	frame_num += 1
 
cap.release()
cv2.destroyAllWindows()
out.release()

