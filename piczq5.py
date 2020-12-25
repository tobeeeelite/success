##伽马变换
import  cv2 as cv
import numpy as np
image =cv.imread(r'D:\pycharm\work\enhancepic\0.jpg')
fi=image/255.0
gamma=0.5
out=np.power(fi,gamma)
cv.imshow('out',out)
cv.waitKey(0)
cv.destroyAllWindows()
# gamma_image = np.power(image / float(np.max(image)), gamma)
# cv.imshow('gamma_image', gamma_image )
# cv.waitKey(0)