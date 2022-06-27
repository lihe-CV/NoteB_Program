import cv2 as cv

img = cv.imread('Photos/2.jpeg')
print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
print(gray.shape)
# shape 所对应的数的个数是图片对应的维度，比如彩色图片是三维的，所以有1333，2000，3这三个数
# 灰度图像是二维的，所以只有1333，2000两个数，而每个数的意义代表在相应维度上的数值个数
