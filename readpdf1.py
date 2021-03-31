# -*- coding: utf-8 -*-
# @Time    : 2021/1/14
# @Author  : jhh
# @File    : readpdf1.py
# @Software: PyCharm
# import pdfminer
# import pdfplumber
# import pandas as pd

# path = r'2.pdf'
# with pdfplumber.open(path) as pdf:
#     first_page = pdf.pages[0]  # 获取第一页
#     print(first_page.extract_text())
# print(1)

from PythonMagick import Image
import cv2 as cv

with Image(filename=r'E:\work\segmentation\2.pdf') as img:
    with img.convert('jpeg') as converted:
        converted.save(filename='image.jpeg')
