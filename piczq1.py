###灰度直方图
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def calcGrayHist(img):
    h, w = img.shape[:2]
    grayHist = np.zeros([256], np.uint8)
    for i in range(h):
        for j in range(w):
            grayHist[img[i][j]] += 1
    return grayHist


img = cv.imread('hello1.png', 0)
grayHist = calcGrayHist(img)
x = np.arange(256)
plt.plot(x, grayHist, 'r', linewidth=2, c='black')
plt.xlabel('gray label')
plt.ylabel('number of pixels')
plt.show()
