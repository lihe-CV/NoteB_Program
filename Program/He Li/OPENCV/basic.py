import cv2 as cv

img = cv.imread('Photos/rubbish_2.jpg')
cv.imshow("rubbish", img)

# Converting to grayscale (灰度变换)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRAY", gray)

# Blur (模糊)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade(边缘级联), 可以通过对图像进行模糊从而减少无关边缘的获取
# canny = cv.Canny(img, 125, 175)  # 获取清晰图像
canny = cv.Canny(blur, 125, 175)  # 获取模糊图像
cv.imshow("Canny Edges", canny)

# Dilating the image (膨胀)
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("Dilated", dilated)

# Eroding (腐蚀)
eroded = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("Eroded", eroded)

# Resize (图像大小调整) ? 最后一个参数的区别
resized = cv.resize(img, (200, 200), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize', resized)


# Cropping (图像裁剪)
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
