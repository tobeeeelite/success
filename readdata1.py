##批量读取图片
import cv2 as cv
import os
import numpy as np
array_img=[]
def read_path(file_pathname):
    for filename in os.listdir(file_pathname):
        img=cv.imread(file_pathname+"/"+filename)
        array_img.append(img)
read_path(r'D:\pycharm\work\data')
print(array_img[0])
print(len(array_img))
cv.imshow('3',array_img[68029])
cv.waitKey(0)
cv.destroyAllWindows()

