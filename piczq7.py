##对数变换
import cv2 as cv
import numpy as np
img=cv.imread('hello1.png')
output_img=100*np.log(1.0+img)
output_img=np.uint8(output_img+0.5)
cv.imshow('out',output_img)
cv.imshow('input',img)
cv.waitKey(0)