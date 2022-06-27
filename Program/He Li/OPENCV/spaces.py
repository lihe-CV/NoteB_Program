# 色彩空间, 如何在opencv中实现颜色空间之间切换,表示像素颜色阵列的系统。
# BGR(opencv中是)(RGB, 将BGR转化成RGB) 是色彩空间。 灰度是一种色彩空间。 我们还有其他颜色空间，如 HSV、LAB等等。
# HSV: H: 色调, 取值范围0——360从红色按逆时针方向计算, 红色为0, 绿色为120
#         蓝色为240，对应的补色, 黄色为60, 青色为180, 品红为300.
#      S: 饱和度, 表示颜色接近光谱色的程度. 颜色可以看成光谱色和白色混合的效果.
#         其中光谱色所占的比例愈大，颜色接近光谱色的程度就愈高，颜色的饱和度也就愈高.
#         饱和度高，颜色则深而艳。光谱色的白光成分为0，饱和度达到最高.
#         通常取值范围为0%～100%，值越大，颜色越饱和。
#      V: 明度, 表示颜色明亮程度, 对于光源色，明度值与发光体的光亮度有关；
#         通常取值范围为0%（黑）到100%（白）.

import cv2 as cv
import matplotlib.pyplot as plt

# 初始化
img = cv.imread('Photos/rubbish_1.png')
cv.imshow('rubbish', img)
# plt.imshow(img) 由于plt读取的是RGB图片, 所以plt展示cv读取的BGR图片时，会和原图红变蓝，蓝变红.


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB(L*a*b) LAB 格式更多地转向人类的感知方式, 是BGR 图像的冲洗版本
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

cv.waitKey(0)