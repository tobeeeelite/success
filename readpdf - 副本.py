# -*- coding: utf-8 -*-
# @Time    : 2021/1/14
# @Author  : jhh
# @File    : readpdf.py
# @Software: PyCharm

import pdfplumber
import pandas as pd
with pdfplumber.open("1.pdf") as pdf:
    page = pdf.pages[0]   # 第一页的信息
    text = page.extract_text()
    print(text)
    table = page.extract_tables()
    for t in table:
        # 得到的table是嵌套list类型，转化成DataFrame更加方便查看和分析
        df = pd.DataFrame(t[1:], columns=t[0])
        print(df)



