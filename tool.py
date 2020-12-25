#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/10 9:54
# @Author  : zyg
# @Site    : 
# @File    : tool.py
# @Software: PyCharm

import os
import shutil

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
            if ext  not in ['.pdf','.docx','doc']:
                abs_file.append(os.path.join(root, file))
    return abs_file


def main():
    label = '数学'
    files = get_files(r'D:\小学试题照片')
    for k,f  in enumerate(files) :
        if label in f:
            print(f)
            _, name =  os.path.split(f)
            new_path = os.path.join(r'D:\maths','{0}.jpg'.format(k))
            shutil.copyfile(f,new_path)



if __name__ == '__main__':
    main()