# 本节是关于图像轮廓处理的
"""
cv.findContours函数参数详解：
    原型：findContours( InputOutputArray image, OutputArrayOfArrays contours,
                              OutputArray hierarchy, int mode,
                              int method, Point offset=Point());
    第一个参数, image: 可以为灰度图，但是更长用的是二值化图像
                     一般为经过Canny, 拉普拉斯等边缘检测算子处理过的二值化图像
    第二个参数, contours: vector<vector<Point>> contours 一个双向向量，向量内每个元素保存了一组由连续的Point点构成的点的集合的向量，
                        每一组Point点集就是一个轮廓。 有多少轮廓，向量contours就有多少元素。
    第三个参数, hierarchy: 定义 vector<Vec4i> hierarchy
                         <Vec4i>定义  typedef Vec<int, 4> Vec4i;
                            为一个元素包含了四个int类型变量的向量
                         所以定义上看，hierarchy 是一个向量，向量的元素保存了一个包含4个int类型的数组
                         所以hierarchy[i][0]-hierarchy[i][3]表实i个轮廓的后一个轮廓、前一个轮廓、父轮廓、内嵌轮廓的索引编号
                         没有默认值为-1
    第四个参数, mode: 定义轮廓的检索模式:
                        取值一: CV_RETR_EXTERNAL 只检测最外围轮廓
                        取值二: CV_RETR_LIST 检测所有的轮廓,不建立等级关系, 这个检索模式下不存在父轮廓或内嵌轮廓，
                               所以hierarchy向量内所有元素的第3、第4个分量都会被置为-1
                        取值三: CV_RETR_CCOMP 检测所有轮廓, 只有两个等级关系，顶层与内围（内围还有轮廓定义为顶层)
                        取值四: CV_RETR_TREE 检测所有轮廓，所有轮廓建立一个等级树结构。外层轮廓包含内层轮廓，
                               内层轮廓还可以继续包含内嵌轮廓。
    第五个参数, method: 定义轮廓的近似方法:
                        取值一: CV_CHAIN_APPROX_NONE 保存物体边界上所有连续的轮廓点到contours向量内
                        取值二: CV_CHAIN_APPROX_SIMPLE 仅保存轮廓的拐点信息
    第六个参数, Point: 偏移量, 所有的轮廓信息相对于原始图像对应点的偏移量
"""

import cv2 as cv
import numpy as np

# # 初始化
# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cats', img)
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)
#
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)
#
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)
#
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours)} contours found!')

# 第二种threshold(二值化)方式从而获取轮廓
img = cv.imread('Photos/rubbish_1.png')
cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, herarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

# 将获取的轮廓显现在blank背景下的图片上
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Black', blank)

cv.drawContours(blank, contours, -1, (0, 255, 0), 2)  # -1是指获取全部轮廓集合，2是指轮廓绘制后图片厚度变为2
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
