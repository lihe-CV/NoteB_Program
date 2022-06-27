# 图像融合, 不是通过Open CV实现的

from PIL import Image

img1 = Image.open("Photos/rubbish_5.jpg")
img1 = img1.convert('RGBA')

img2 = Image.open("Photos/rubbish_4.jpg")
img2 = img2.convert('RGBA')
# resize to size of img1
img2 = img2.resize(img1.size)
print(img2.size)

img = Image.blend(img1, img2, 0.4)
img.show()
