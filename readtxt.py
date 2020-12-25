####简单拼接图片
##cv读取的图片是（h,w,c）
##实际图片是(w,h,c)
import cv2 as cv
import numpy as np
img1=cv.imread('gs.png',0)#公式
img2=cv.imread('hello1.png',0)#文本
print(img1.shape)
h,w=img1.shape
h_n,w_s=img2.shape
print(w_s)
w_n=w
if w / h >= w_n / h_n:
    img_new = cv.resize(img1, (w_n, int(w_n * h / w)))
else:
    img_new = cv.resize(img1, (int(h_n * w / h), h_n))
cv.imwrite('n_gs.png',img_new)
cv.imshow('2',img_new)
cv.waitKey(0)
h_nn,w_n=img_new.shape
print(img_new.shape)
img3=np.hstack((img2,img_new))
print(img3.shape)

x_left=w_s
x_right=w_s+w_n
x_location=(x_left,x_right)
print(x_location)
cv.imwrite('3.png',img3)
cv.imshow('3',img3)
cv.waitKey(0)
cv.destroyAllWindows()












