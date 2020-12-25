# -*- coding: utf-8 -*-
# @Time    : 2020/12/19
# @Author  : jhf
# @File    : test02.py
# @Software: PyCharm
import cv2
import numpy as np
import os
img=cv2.imread('test02.jpg',0)
h,w=img.shape[:2]
mask=np.zeros([h+2,w+2],dtype=np.uint8)
img_copy=img.copy()
cv2.floodFill(img_copy,mask,(30,100),(0,0,0))
c=len(np.where(img_copy>127)[0])
print(c)
cv2.imshow('img_copy',img_copy)
cv2.waitKey(0)
# i=10.9
# factor=33
# i = int(i)
# rem = i % factor
# if not rem:
#     print(i)
# else:
#     print(i+factor-rem)

def resize_to_screen(src, maxw=1280, maxh=700, copy=False):
    height, width = src.shape[:2]

    scl_x = float(width) / maxw
    scl_y = float(height) / maxh

    scl = int(np.ceil(max(scl_x, scl_y)))

    if scl > 1.0:
        inv_scl = 1.0 / scl
        img = cv2.resize(src, (0, 0), None, inv_scl, inv_scl, cv2.INTER_AREA)
    elif copy:
        img = src.copy()
    else:
        img = src

    return img
imgfile=(r"D:\pycharm\work\page_dewrap\page_dewarp-master\example_input\TEST\2941.jpg")
outfiles = []
img = cv2.imread(r'D:\pycharm\work\page_dewrap\page_dewarp-master\example_input\TEST\2941.jpg')
GaussianBlur_img = cv2.medianBlur(img, 1)
cv2.imshow('11',GaussianBlur_img)

# if img is None:

    # continue
small = resize_to_screen(GaussianBlur_img)
cv2.imshow('small',small)
cv2.waitKey(0)
name, _ = os.path.splitext(imgfile)
PAGE_MARGIN_X =5  # reduced px to ignore near L/R edge减少px以忽略左/右边缘
PAGE_MARGIN_Y =10      # reduced px to ignore near T/B edge减少px以忽略T / B边缘附近 上下边缘框
height, width = small.shape[:2]
xmin = PAGE_MARGIN_X
ymin = PAGE_MARGIN_Y
xmax = width-PAGE_MARGIN_X
ymax = height-PAGE_MARGIN_Y

page = np.zeros((height, width), dtype=np.uint8)
cv2.rectangle(page, (xmin, ymin), (xmax, ymax), (255, 255, 255), -1)

outline = np.array([
    [xmin, ymin],
    [xmin, ymax],
    [xmax, ymax],
    [xmax, ymin]])
cv2.imshow('page',page)
cv2.waitKey(0)
print(outline)
