import cv2 as cv
import numpy as np
drawing=False
mode=True
ix,iy=-1,-1
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event==cv.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv.rectangle(img,(ix,iy),(x,y),(0,255,0),1)
        else:
            cv.circle(img,(x,y),abs(x-ix),(0,0,255),1)
img=np.zeros((512,512,3),np.uint8)
img[:,:,0]=np.ones([512,512])*255
img[:,:,1]=np.ones([512,512])*255
img[:,:,2]=np.ones([512,512])*255
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)
while(1):
    cv.imshow('image',img)
    if cv.waitKey(20)&0xFF==27:
        break
    elif cv.waitKey(20)&0xFF==ord('m'):
        mode=not mode
cv.destroyAllWindows()
# events=[i for i in dir(cv) if 'EVENT'in i]
# print (events)