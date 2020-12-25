#限制对比度的自适应直方图均衡化
import cv2 as cv
img=cv.imread(r'D:\pycharm\work\enhancepic\0.jpg',0)
clahe=cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
dst=clahe.apply(img)
equa=cv.equalizeHist(img)
cv.imshow('img',img)
cv.imshow('dst',dst)
cv.imshow('equa',equa)
cv.waitKey(0)
cv.destroyAllWindows()