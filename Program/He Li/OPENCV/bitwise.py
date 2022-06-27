# 本节是关于图像的按位运算(bitwise operations) 操作

import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1) # -1使得厚度可以充满整个矩形区域
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle', circle)

# bitwise AND: 把这两个图像放在彼此的顶部，基本上返回了交集.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise_And', bitwise_and)

# bitwise OR: 返回并集
bitwise_or= cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise_Or', bitwise_or)

# bitwise XOR: 返回不相交区域
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise_Xor', bitwise_xor)

# bitwise NOT: 反转二进制颜色
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle_Not', bitwise_not)


cv.waitKey(0)