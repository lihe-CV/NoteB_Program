# 本节是关于使用opencv完成图像的直方图计算
# 直方图基本上允许您可视化图像中像素强度的分布
# calcHist(images, channels,
#          mask, histSize,
#          ranges, hist=None, accumulate=None)
# images: 输入的图像组或数组，深度必须为CV_8U, CV_16U或CV_32F中一种
#         尺寸必须相同, 输入时用[]括起来
# channels: 传入图像的通道数, 灰度图像通道数为0; 彩色图像的话, 可以0,1,2之间选择,
#           对应的分别是b, g, r通道
# mask: 掩膜图像。如果是计算整幅图, 为none。主要是如果要统计部分图的直方图,
#       就得构造相应的炎掩膜来计算
# histSize: 灰度级的个数, 需要中括号
# ranges: 像素级的范围, 通常为[0,256]

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(img, img, mask=circle)  # gray histogram 将 img 改成 gray
cv.imshow('Mask', mask)

# # histogram from gray image
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
#
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')  # 像素点取值
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')  # 像素点取值
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim(0, 255)

plt.show()


cv.waitKey(0)