import cv2 as cv
import numpy as np
img_path=r'E:\work\unet-denoising-dirty-documents-master\images\1.jpg'
img=cv.imread(img_path)

a= np.array(img)
Blur_img = cv.GaussianBlur(img, (77, 77), 50)
b = np.array(Blur_img)

c = a / b
# c[np.where(b=0)]=0

# cv.imwrite(r'%d.jpg' % (10), c*255 )
cv.imshow('c',c)
cv.waitKey(0)