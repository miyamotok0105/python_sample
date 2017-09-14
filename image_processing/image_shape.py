import cv2
import numpy as np
from PIL import Image

def rgb2gray(rgb):
    return np.dot(rgb[...,:4], [0.299, 0.587, 0.114])

def rgb2gray2(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray[np.newaxis, :]


path_jpg = "img/shougi.jpg"
path_png = "img/shougi.png"
image = np.asarray(Image.open(path_jpg))
print(image.shape)
image = np.asarray(Image.open(path_png))
print(image.shape)

print(image.transpose(2, 0, 1).shape)

image = np.asarray(Image.open(path_png).resize((256,256,)))
print(image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(gray_image.shape)
# image = np.asarray(Image.open(path)).transpose(2, 0, 1)

image = np.asarray(Image.open(path_png))
gray = rgb2gray(image)    
print(gray.shape)

print("rgb2gray2")
image = np.asarray(Image.open(path_png))
gray = rgb2gray2(image)    
print(gray.shape)
