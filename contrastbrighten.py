# -*- coding: utf-8 -*-
# @Time    : 2020/12/23
# @Author  : jhf
# @File    : contrastbrighten.py
# @Software: PyCharm
def contrast_brighten(image):
    win_size=50
    nw=image.shape[1]/win_size
    nh=image.shape[0]/win_size
    for i in range(0,nh+1):
        for j in range(0,nw+1):
            rstart=i*win_size
            cstart=j*win_size

            rend = rstart + win_size
            cend = cstart + win_size
            if rend<image.shape[0]:
                return rend
            else:
                rend=image.shape[0]
            if cend < image.shape[1]:
                return cend
            else:
                rend = image.shape[1]