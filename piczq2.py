#全局直方图均衡化

import cv2 as cv
image=cv.imread(r'D:\pycharm\work\enhancepic\0.jpg')
gray=cv.cvtColor(image,cv.COLOR_RGB2GRAY)
dst=cv.equalizeHist(gray)
print(dst.shape)
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()

