# 将讨论如何使用各种模糊技术平滑和模糊图像
# 平滑图像是因为图像有很多噪声, 噪声的产生分外部噪声和内部噪声：
#   外部噪声，即指系统外部干扰以电磁波或经电源串进系统内部而引起的噪声. 如电气设备, 天体放电现象等引起的噪声.
#   内部噪声：一般又可分为以下四种:
#       （1）由光和电的基本性质所引起的噪声.
#       （2）电器的机械运动产生的噪声.
#       （3）器材材料本身引起的噪声.
#       （4）系统内部设备电路所引起的噪声.
# kernel: kernel size 和窗口的行数与列数相关, 如果一个窗口有三行三列, 他的kernel size的大小就是3*3
# blur 就是将窗口中间的像素作为包围这个像素的整体像素的结果，也叫做周围像素.
# 滤波窗口内，距离中心点越近的点的权重越大; 这种只关注距离的思想在某些情况下是可行的,
# 例如在平坦的区域，距离越近的区域其像素分布也越相近, 自然地，这些点的像素值对滤波中心点的像素值更有参考价值.
# 但是在像素值出现跃变的边缘区域，这种方法会适得其反，损失掉有用的边缘信息。此时就出现了一类算法——边缘保护滤波方法
# 算法思想很简单，在高斯滤波的基础上加入了像素值权重项，也就是说既要考虑距离因素，也要考虑像素值差异的影响
# 双边滤波：
#   void bilateralFilter( InputArray src, OutputArray dst, int d,
#                                    double sigmaColor, double sigmaSpace,
#                                    int borderType = BORDER_DEFAULT );
#   src: 表示输入图像
#   dst: 表示输出图像
#   d: 表示滤波窗口的直径, 此函数中选取的窗口是圆形
#   sigmaColor: 像素值域方差, 意味着邻域中有更多颜色，但会在计算模糊时考虑.
#   sigmaSpace: 空间域方差, 此值越大, 表明计算中心点像素的时候附近需要参与计算的像素越多
#               如果 d 的值大于0则无效，否则根据它来计算 d 值

import cv2 as cv

img = cv.imread('Photos/mask.jpg')
cv.imshow('rubbish', img)

# Averaging: 在图像的特定部分定义了一个内核窗口
#           这个窗口将使用所有周围像素强度的平均值作为像素的中心值,
#           只保留中心值, 后窗口向右移动, 后向下移动
#           和卷积的计算相似, 所以kernel size 的大小越大, 模糊程度越高
average = cv.blur(img, (3, 3))
cv.imshow('Average', average)

# Gaussian Blur: 与Averaging不同的是周围的像素都被赋予一个特定的权重
#                而不是计算平均值, 所以他的模糊度没有Averaging那么强
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur 与Averaging基本一致, 除了它不是查找周围像素的平均值, 而是查找周围像素的中值.
#             通常, 这种方式在去除噪声方面有更好的效率.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral 这个算法的效率最高
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)