##直方图正规化

import cv2 as cv
import numpy as np
img=cv.imread(r'D:\pycharm\work\enhancepic\0.jpg')
img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
Imin,Imax=cv.minMaxLoc(img1)[:2]
Omin,Omax=0,255
a=float(Omax-Omin)/(Imax-Imin)
b=Omin-a*Imin
out=a*img+b
out=out.astype(np.uint8)
cv.imshow('img',img1)
cv.imshow('out',out)
cv.waitKey(0)
cv.destroyAllWindows()