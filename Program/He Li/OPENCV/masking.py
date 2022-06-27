# 将在称为掩码的概念中讨论如何使用这些按位运算.
# 掩蔽可以使我们集中于观看图像中的重点部分

import cv2 as cv
import numpy as np

img = cv.imread('Photos/rubbish.jpg')
cv.imshow('Rubbish', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2-100, img.shape[0]//2-100), (img.shape[1]//2, img.shape[0]//2), 255, -1)
cv.imshow('Rectangle', rectangle)

mask = cv.bitwise_and(rectangle,circle)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Image', masked)

cv.waitKey(0)