#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

## 3x4の行列を作成
a = np.arange(12).reshape(3,4)
print("a:", a)
print("各行の総和：", a.sum(axis=0))
print("各列の総和：", a.sum(axis=1))
print("要素の抽出：", a[0,2], a[0,3])
print("------------")
b = np.array([[1, 2], [3, 4]])
c = np.array([[5, 6]])
print("bにcを行結合", np.concatenate((b, c), axis=0))
print("bにcを列結合", np.concatenate((b, c.T), axis=1))
print("------------")
d = (1, 2, 3, 4)
print("d:", d)
print("d array:", np.array(d))
print("d shape:", np.array(d).shape)
print("dの1〜4要素：", np.array(d)[1:4,])
print("------------")
e = np.array([1, 2, 3, 4])
print("e shape:", e.shape)
print("type:", type(e))
print("eの1〜4要素：", d[1:3])
print("------------")
f = np.arange(196608).reshape(1,256,256,3)
# print("f:", f)
print("f shape:", f.shape)
print(f.reshape(1,2,3).shape)
# print(f.transpose(1, 2, 3, 0).shape)
# print(np.delete(f, 0, 1).shape)






