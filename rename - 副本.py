# -*- coding: utf-8 -*-
# @Time    : 2021/1/25
# @Author  : jhf
# @File    : rename.py
# @Software: PyCharm
import os
file_pathname=(r'E:\work\segmentation\1')
filelist=os.listdir(file_pathname)
total_num=len(filelist)
i=0
for item in filelist:
    src=os.path.join(os.path.abspath(file_pathname),item)
    # dst=os.path.join(os.path.abspath(file_pathname),str('66_dark_3_')+str(i)+'.jpg')
    dst = os.path.join(os.path.abspath(file_pathname), str(i) + '.jpg')
    try:
        os.rename(src,dst)
        i+=1
    except:
        continue
print('total%d to rename&converted %d jpgs'%(total_num,i))