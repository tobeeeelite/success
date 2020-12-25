# -*- coding: utf-8 -*-
# @Time      :2020/12/24
# @Author   : jhf
# @File     : enhance3.py
# @Software : PyCharm
import cv2 as cv
import numpy as np
image=cv.imread(r'D:\pycharm\work\pic\1608262058470.jpg')
gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
Imin,Imax=cv.minMaxLoc(gray_image)[:2]
Omin,Omax=0,255
a=float(Omax-Omin)/(Imax-Imin)
b=Omin-a*Imin
out_img=a*gray_image+b
out_img=out_img.astype(np.uint8)
blur_img=cv.GaussianBlur(out_img,(5,5),51)
# blur_img=cv.blur(gray_image,(7,7))
threshold_img=cv.adaptiveThreshold(blur_img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,4)
horizontalKernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
erode_img = cv.morphologyEx(threshold_img, cv.MORPH_ERODE, horizontalKernel)
gamma=4.0
gamma_image = np.power(threshold_img / float(np.max(image)), gamma)
cv.imshow('threshold_img',threshold_img)
cv.imshow('erode_img',gamma_image)
cv.waitKey(0)
cv.destroyAllWindows()