#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 15:36
# @Author  : zyg
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import os
import cv2
import numpy as np

def get_files(in_dir):
    #print('get train_data files  from  '+exts)
    files = []
    if not os.path.exists(in_dir):
        ValueError("visit path is not exits")
    abs_file = []
    for root, _, files in os.walk(in_dir):
        for file in files:
            _ ,ext = os.path.splitext(file)
            # print(ext)
            if ext not in ['.pdf','.docx','doc']:
                abs_file.append(os.path.join(root, file))
    return abs_file







def main():
    files = get_files(r'E:\OCR\page_dewrap\page_dewarp-master\test')
    for k,img_name in files:
        if not os.path.exists(img_name):
            continue
        img = cv2.imread(img_name)







if __name__=='__main__':
    main()
