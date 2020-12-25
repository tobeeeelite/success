# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : jhf
# @File    : enhance2.py
# @Software: PyCharm
import cv2 as cv
import numpy as np
import math

# def unevenLightCompensate(img, blockSize):
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     average = np.mean(gray)
#
#     rows_new = int(np.ceil(gray.shape[0] / blockSize))
#     cols_new = int(np.ceil(gray.shape[1] / blockSize))
#
#     blockImage = np.zeros((rows_new, cols_new), dtype=np.float32)
#     for r in range(rows_new):
#         for c in range(cols_new):
#             rowmin = r * blockSize
#             rowmax = (r + 1) * blockSize
#             if (rowmax > gray.shape[0]):
#                 rowmax = gray.shape[0]
#             colmin = c * blockSize
#             colmax = (c + 1) * blockSize
#             if (colmax > gray.shape[1]):
#                 colmax = gray.shape[1]
#
#             imageROI = gray[rowmin:rowmax, colmin:colmax]
#             temaver = np.mean(imageROI)
#             blockImage[r, c] = temaver
#
#     blockImage = blockImage - average
#     blockImage2 = cv2.resize(blockImage, (gray.shape[1], gray.shape[0]), interpolation=cv2.INTER_CUBIC)
#     gray2 = gray.astype(np.float32)
#     dst = gray2 - blockImage2
#     dst = dst.astype(np.uint8)
#     dst = cv2.GaussianBlur(dst, (3, 3), 0)
#     dst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
#
#     return dst

# if __name__ == '__main__':
#     file = r'D:\pycharm\work\enhancepic\0.jpg'
#
#     blockSize = 16
#     img = cv2.imread(file)
#     dst = unevenLightCompensate(img, blockSize)
#
#     result = np.concatenate([img, dst], axis=1)
#
#     cv2.imshow('result', result)
#     cv2.waitKey(0)
def gamma_img(img,gamma):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    a=cv.LUT(image, table)
    cv.imshow('a',a)
    cv.waitKey(0)
    return a

# 读取图像
# image=cv.imread(r'D:\pycharm\work\enhancepic\0.jpg').astype('uint8')
image=cv.imread(r'D:\pycharm\work\enhancepic\1.jpg')
# image=cv.imread(r'D:\pycharm\work\enhancepic\1608262000449.jpg')
gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
Imin,Imax=cv.minMaxLoc(gray_image)[:2]
Omin,Omax=0,255
a=float(Omax-Omin)/(Imax-Imin)
b=Omin-a*Imin
out_img=a*gray_image+b
out_img=out_img.astype(np.uint8)
# horizontalKernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# erode_img = cv.morphologyEx(out_img, cv.MORPH_ERODE, horizontalKernel)
blur_img=cv.GaussianBlur(out_img,(7,7),51)
threshold_img = cv.adaptiveThreshold(blur_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
gamma=4.0
gamma_image = np.power(threshold_img / float(np.max(image)), gamma)
cv.imshow('threshold_img',threshold_img)
cv.imshow('gimg',gamma_image)
cv.waitKey(0)
cv.destroyAllWindows()
# gamma=4.0
# # gamma_img(image,gamma)

# b, g, r = cv.split(image)
# b_avg = cv.mean(b)[0]
# g_avg = cv.mean(g)[0]
# r_avg = cv.mean(r)[0]
#
# # 求各个通道所占增益
# k = (b_avg + g_avg + r_avg) / 3
# kb = k / b_avg
# kg = k / g_avg
# kr = k / r_avg
#
# b = cv.addWeighted(src1=b, alpha=kb, src2=0, beta=0, gamma=0)
# g = cv.addWeighted(src1=g, alpha=kg, src2=0, beta=0, gamma=0)
# r = cv.addWeighted(src1=r, alpha=kr, src2=0, beta=0, gamma=0)
#
# balance_img = cv.merge([b, g, r])
# cv.imshow('balance_img',balance_img)
# cv.waitKey(0)
