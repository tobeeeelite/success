# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : jhf
# @File    : gaussian1.py
# @Software: PyCharm
import cv2 as cv
import numpy as np

img=cv.imread(r'D:\pycharm\work\enhancepic\0.jpg')
b=cv.GaussianBlur(img,(31,31),51)
b=np.array(b)
a=np.array(img)
c=a-b+127
cv.imshow('c',c*255)
cv.waitKey(0)