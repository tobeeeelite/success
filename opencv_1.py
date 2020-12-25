import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
img[:,:,0]=np.ones([512,512])*255
img[:,:,1]=np.ones([512,512])*255
img[:,:,2]=np.ones([512,512])*255
# cv.line(img,(10,10),(500,10),(255,255,255),1)
# cv.line(img,(10,10),(10,500),(255,255,255),1)
# cv.line(img,(10,500),(500,500),(255,255,255),1)
# cv.line(img,(500,10),(500,500),(255,255,255),1)
cv.rectangle(img,(10,10),(500,500),(0,255,0),3)##画矩形 第一个是左顶点 第二个是右下角的顶点坐标
cv.circle(img,(255,255),255,(255,255,0),3)##画圆 需要知道圆心坐标和半径长度
cv.ellipse(img,(256,256),(100,50),0,0,360,(255,0,255),-1)#画椭圆
###画多边形
# pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
# pts=pts.reshape((-1,1,2))
# cv.polylines(img,[pts],True,(0,255,0))## 可以被用来画很多条线。只需要把想要画的线放在一
# 个列表中，将这个列表传给函数就可以了。每条线都会被独立绘制。这会比用
# cv2.line() 一条一条的绘制要快一些。
font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Hi',(10,500),font,4,(0,0,255),2)

cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()