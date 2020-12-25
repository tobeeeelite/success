##英语字符加公式图片
import cv2 as cv
import numpy as np
img1=cv.imread('hello.png',0)
img2=cv.imread('gs.png',0)
# up=cv.pyrUp(img2)
# down=cv.pyrDown(img2)
# h,w=down.shape
h,w=img2.shape

print(h,w)
# cv.imshow('d',down)
# cv.waitKey(0)
h_n,w_s=img1.shape
w_n=w
# img_new=cv.resize(down,(w,h_n))
if w/h>=w_n/h_n:
    img_new=cv.resize(img2,(w_n, int(w_n * h / w)))
else:
    img_new=cv.resize(img2,(int(h_n * w / h), h_n))
img3=np.hstack((img1,img_new))
w_new=img_new.shape[1]
x_left=w_s
print(img3.shape)
x_right=img3.shape[1]
x_location=(x_left,x_right)
print(x_location)
cv.imwrite('rh1.png',img3)
cv.imshow('4',img3)
cv.waitKey(0)
cv.destroyAllWindows()