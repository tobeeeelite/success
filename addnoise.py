##添加噪声
import cv2 as cv
import random
im=cv.imread('hello1.png')
for k in range(100):
    i=random.randint(0,im.shape[0]-1)
    j=random.randint(0,im.shape[1]-1)
    color=(random.randrange(256),random.randrange(256),random.randrange(256))
    im[i,j]=color
cv.imshow('11',im)
cv.waitKey(0)