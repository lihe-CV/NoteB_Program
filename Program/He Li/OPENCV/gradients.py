# 讨论如何计算图像中的梯度和边缘.
# 从数学角度来看, 梯度和边缘是两个不同的概念,
# 然而仅从编程的角度来看, 几乎可以将梯度视为边缘.

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian: 图像本身不能具有负像素值。
#            所以我们所做的是本质上计算该图像的绝对值。
#            所以图像的所有像素值都被转换为绝对值。
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel: Sobel gradient magnitude representation(Sobel 梯度幅值表示)
#        Sobel 在两个方向上计算梯度(x, y)
#        Y 水平
#        X 竖直
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # 第三个参数表示x方向,第四个表示y方向, 取1表示计算, 0表示不计算
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)  # 一种更高级的算法, 在其中一个阶段使用了 Sobel。
cv.imshow('Canny', canny)


cv.waitKey(0)