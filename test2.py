import cv2
import numpy as np
from PIL import Image

# 灰度图片进行二值化处理
# img = cv2.imread('paper_0_0.png')
# GrayImage = cv2.cvtColor(img[:, 457:807, :], cv2.COLOR_BGR2GRAY)
# _, thresh1 = cv2.threshold(GrayImage, 130, 255, cv2.THRESH_BINARY)
# _, thresh2 = cv2.threshold(GrayImage, 130, 255, cv2.THRESH_BINARY)
#
# # 水平投影
# (h, w) = thresh1.shape
# a = [0 for z in range(0, h)]
# for j in range(0, h):
#     for i in range(0, w):
#         if thresh1[j, i] == 0:
#             a[j] += 1
#             thresh1[j, i] = 255
# for j in range(0, h):
#     for i in range(0, a[j]):
#         thresh1[j, i] = 0
#
# # 垂直投影
# (h, w) = thresh2.shape
# a = [0 for z in range(0, w)]
# for j in range(0, w):
#     for i in range(0, h):
#         if thresh2[i, j] == 0:
#             a[j] += 1
#             thresh2[i, j] = 255
# for j in range(0, w):
#     for i in range((h - a[j]), h):
#         thresh2[i, j] = 0
#
# # 展示图片
# cv2.imshow("src", img)
# cv2.imshow('img', thresh1)
# cv2.imshow('img2', thresh2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 垂直投影
import numpy as np
import cv2 as cv

img = cv.imread("paper_0_0.png", 0)
ret, img1 = cv.threshold(img, 80, 255, cv.THRESH_BINARY)

# 返回图像的高和宽
(h, w) = img1.shape

# 初始化一个跟图像宽一样长度的数组，用于记录每一列的黑点个数
a = [0 for z in range(0, w)]

for i in range(0, w):  # 遍历每一列
    for j in range(0, h):  # 遍历每一行
        if img1[j, i] == 0:  # 判断该点是否为黑点，0代表是黑点
            a[i] += 1  # 该列的计数器加1
            img1[j, i] = 255  # 记录完后将其变为白色，即等于255
for i in range(0, w):  # 遍历每一列
    for j in range(h - a[i], h):  # 从该列应该变黑的最顶部的开始向最底部设为黑点
        img1[j, i] = 0  # 设为黑点
cv.imshow("img", img1)
cv.waitKey(0)
cv.destroyAllWindows()
