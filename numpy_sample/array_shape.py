# -*- coding: utf-8 -*-
import numpy as np

a = np.array([[1, 2]])
print(a)
print(a.shape)
print("---------")
a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)
print("---------")
#配列のスライス
print("array slice ", a[:,:])
print("---------")
#配列のスライス
print("array slice ", a[:,0])
print(a[:,1])
print("---------")
arr3 = np.array([[[0 for i3 in range(5)] for i2 in range(4)] for i1 in range(3)])
print(arr3.shape)
print("---------")
arr3[:, :, 0] = 1
print("[:, :, 0] slice:", arr3)
arr3[:, :, 0] = 0
arr3[:, 0, :] = 1
print("---------")
print("[:, 0, :] slice:", arr3)
arr3[:, 0, :] = 0
arr3[0, :, :] = 1
print("---------")
print("[0, :, :] slice:", arr3)

