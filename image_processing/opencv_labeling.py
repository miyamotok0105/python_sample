# -*- coding: utf-8 -*-
#use:
#python opencv_labeling.py img/520f8a8d.jpg

import cv2
import numpy as np
import sys

args = sys.argv

image_path = ""
if len(args) < 2:
    image_path = "img/520f8a8d.jpg"
else:
    image_path = str(args[1])

img = cv2.imread(image_path)

def main():
    # 入力画像の取得
    im = cv2.imread(image_path)
    # グレースケール変換
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # 2値化
    # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO | cv2.THRESH_OTSU)[1]

    # ラベリング処理
    n, label = cv2.connectedComponents(gray)
    # ラベルの個数nだけ色を用意
    rgbs = np.random.randint(0,255,(n+1,3))

    # print(type(label))
    # print(len(label))
    for arr in label:
        print(np.count_nonzero(arr))


    # ラベル付けした各マスクを色付け
    for y in xrange(0, gray.shape[0]):
        for x in xrange(0, gray.shape[1]):
            if label[y, x] > 0:
                im[y, x] = rgbs[label[y, x]]
            else:
                im[y, x] = [0, 0, 0]

    while(1):
        # cv2.imshow("Labeling", gray)

        # ウィンドウ表示
        cv2.imshow("Labeling", im)

        # qを押したら終了
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

