# 如何在opencv中拆分和合并颜色通道
# 现在 opencv 允许您将图像拆分为其各自的颜色通道

import cv2 as cv
import numpy as np

img = cv.imread('Photos/10.JPG')
cv.imshow('scenery', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# 将BGR三通道图片转换为b,g,r三个通道的图片
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.imshow('Blue Of Gray', b)
cv.imshow('Green Of Gray', g)
cv.imshow('Red Of Gray', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# 将转换后的三个通道的图片合并为BGR三通道的图片
merged = cv.merge([b, g, r])
cv.imshow('Merge', merged)

cv.waitKey(0)