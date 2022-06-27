# 关于图像阈值化的讨论
# 阈值化是图像的二进制实现 (二值化)
# 定义一个threshold value , 此值和像素通道的取值相比, 如果像素通道取值低于此值，将会变成0.
#   同理，如果大于此值的话, 将会定义为255.
# 图像阈值化分为: 简单阈值化, 自适应阈值化
# 简单阈值化中, 最后一个参数取值:
#   cv.THRESH_BINARY: 普通取值, 图像变为二值化图像, 大于为255, 小于为0
#   cv.THRESH_BINARY_INV: 相反取值, 图像变为二值化图像, 大于为0, 小于为255
# 自适应阈值化: 让计算机自己找到最优阈值:
#   cv2.adaptiveThreshold(src, maxValue, adaptiveMethod,
#                         thresholdType, blockSize, C, dst=None)
#   函数大致意思就是把图片每个像素点作为中心取N*N的区域，然后计算这个区域的阈值，
#   来决定这个像素点变0还是变255.
#   src: 需要进行二值化的灰度图像
#   maxValue: 满足条件的像素点需要设置的灰度值。（将要设置的灰度值）
#   adaptiveMethod: 自适应阈值算法。可选ADAPTIVE_THRESH_MEAN_C
#                   或 ADAPTIVE_THRESH_GAUSSIAN_C
#       ADAPTIVE_THRESH_MEAN_C: 为局部邻域块(kernel)的平均值,
#                               该算法是先求出块中的均值
#                               将均值作为此块的所有像素点的
#                               threshold value.
#       ADAPTIVE_THRESH_GAUSSIAN_C: 为局部邻域块(kernel)的高斯加权和。
#                                   该算法是在区域中(x, y)周围的像素根据
#                                   高斯函数按照他们离中心点的距离进行加权计算
#                                   将结果作为此块的所有像素点的
#                                   threshold value.
#   thresholdType(阈值化类型): 只能THRESH_BINARY或者THRESH_BINARY_INV
#   blocksize: 算法计算邻域时的邻域大小, 即核的大小
#   C: 邻域计算出阈值(threshold value)后再减去C作为最终阈值.

import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cloth', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple Thresholding:返回的第二个参数是二值化图片, 第一个参数是大于threshold value的像素通道数值的个数
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Sample Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', adaptive_thresh)


cv.waitKey(0)
