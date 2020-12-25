# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : jhf
# @File    : enhance1.py
# @Software: PyCharm
import cv2 as cv
import numpy as np
import os
img_array1 = []
file_pathname = r'D:\pycharm\work\enhancepic'
for file in os.listdir(file_pathname):
    img = cv.imread(file_pathname + '/' + file)
    img_array1.append(img)
a = []
blur_img = []
b = []
c= []
d=[]
gamma = 3.0
for i in range(0, len(img_array1)):
    a1 = np.array(img_array1[i])
    a.append(a1)

    Blur_img = cv.GaussianBlur(img_array1[i], (51, 51), 80)
    blur_img.append(Blur_img)
    b1 = np.array(blur_img[i])
    b.append(b1)
    c1 = a[i] / b[i]
    c.append(c1)
    cv.imwrite(r'D:\pycharm\work\enhanced/%d.jpg' % (i), c1*255 )
