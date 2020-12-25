# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : jhf
# @File    : enhance2.py
# @Software: PyCharm
import cv2 as cv
import numpy as np
def yuvzq(image):
    img=cv.cvtColor(image,cv.COLOR_BGR2YUV)
    Y,U ,V=cv.split(img)
    blur_img = cv.GaussianBlur(Y, (7, 7), 100)
    dst = cv.adaptiveThreshold(blur_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                         cv.THRESH_BINARY, 11, 2)
    cv.imshow('dst',dst)
    cv.waitKey(0)
    return dst
if __name__=='__main__':
    # image=cv.imread(r'D:\pycharm\work\enhancepic\1.jpg')
    image=cv.imread(r'D:\pycharm\work\enhancepic\1608262000449.jpg')
    yuvzq(image)