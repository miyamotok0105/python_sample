# -*- coding: utf-8 -*-
#http://takamints.hatenablog.jp/entry/2015/03/04/223059
import numpy as np
import cv2

cols = 640
rows = 480

image = np.zeros([rows,cols,3])

image[:,:,0] = np.ones([rows,cols])*255
image[:,:,1] = np.ones([rows,cols])*255
image[:,:,2] = np.ones([rows,cols])*255

r,g,b = cv2.split(image)
image = cv2.merge([b,g,r])


#-----------------------------------------------
#イメージ生成
# image = np.zeros((rows, cols, 3), np.uint8)


# div = 4 # 縦横の分割数 
# w = cols / div # 分割された領域の横幅
# h = rows / div # 分割された領域の縦幅
# for segrow in xrange(div):
#     y1 = segrow * h # 分割領域上
#     y2 = y1 + h     # 分割領域下
#     c1 = (segrow + 1) * 256 / div - 1   # 色値1
#     for segcol in xrange(div):
#         x1 = segcol * w #分割領域左
#         x2 = x1 + w     #分割領域右
#         c2 = (segcol + 1) * 256 / div - 1   # 色値2
#         s = (segrow + segcol) * 4 + 2       # ステップ
        
#         #(x1,y1)-(x2,y2)の矩形を塗りつぶす
#         image[y1:y2, x1:x2] = [c1/2, c2/2, 0]

#         m = (segrow*div+segcol) % 4
#         if m == 0:
#             #等間隔に別色で点を打つ
#             image[y1:y2:s,x1:x2:s] = [(c1+c2)/2, c1, c2]
#         elif m == 1:
#             # 等間隔の水平線
#             image[y1:y2:s,x1:x2] = [(c1+c2)/2, c1, c2]
#         elif m == 2:
#             # 等間隔の垂直線
#             image[y1:y2,x1:x2:s] = [(c1+c2)/2, c1, c2]
#         elif m == 3:
#             # 等間隔の斜め線
#             for i in xrange(s):
#                 image[y1+i:y2+i:s,x1+i:x2+i:s] = [(c1+c2)/2, c1, c2]

# 表示して[ESC]が押されるまで待つ
cv2.imshow("image", image)
while cv2.waitKey(33) != 27:
    pass

