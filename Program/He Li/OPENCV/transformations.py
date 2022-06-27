# 本节涵盖基本的图像转换，包括平移、旋转、调整大小、翻转、裁剪


import cv2 as cv
import numpy as np


# Translation (平移)
# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # 平移矩阵
    dimensions = (img.shape[1], img.shape[0])  # 维度
    return cv.warpAffine(img, transMat, dimensions)


# Rotation (旋转)
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)
    return cv.warpAffine(img, rotMat, dimension)


# 初始化图像
img = cv.imread('Photos/rubbish_4.jpg')
cv.imshow('rubbish', img)

# Translation (平移)
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation (旋转)
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

# Resizing (调整大小) 如果要缩小图片,将参数调整为INTER_AREA, 如果放大图片,将参数调整为INTER_CUBIC 或者 INTER_LINEAR, CUBIC可能处理图片慢一些,但是效果更好.
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)  # INTER_CUBIC, INTER_LINEAR
cv.imshow("Resized", resized)

# Flip (翻转) flipCode参数可以取0(vertically),1(horizontally),-1(vertically and horizontally)
filp = cv.flip(img, 1)
cv.imshow('Flip',filp)

# Cropping (剪裁)
cropped = img[100:200, 100:200]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
