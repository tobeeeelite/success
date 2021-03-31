import cv2 as cv
import numpy as np


def picture_pdf_detect(img):

    gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imh,imw=gray_img.shape
    _, timg = cv.threshold(gray_img, 127, 255,  cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(7,7))
    opening = cv.morphologyEx(timg, cv.MORPH_ERODE, kernel)
    kernel1=cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dilate_img=cv.morphologyEx(opening,cv.MORPH_DILATE,kernel1)
    # kernel = np.ones((1, 1), np.uint8)
    # opening = cv.morphologyEx(opening, cv.MORPH_DILATE, kernel, iterations=1)
    cv.imshow('op',dilate_img)
    cv.waitKey(0)
    n,labels,stats,_=cv.connectedComponentsWithStats(opening,connectivity=8)
    # cv.imshow('ro',img[113:113+16,2582:2582+27])
    cv.waitKey(0)
    for i in range(n):
        if i==0:
            continue
        x,y,w,h,_=stats[i]
        if w>imw/12:
            sub_region=gray_img[y:y+h,x:x+w]
            cv.imshow('sr',sub_region)
            cv.waitKey(0)

    return  n ,stats



if __name__=="__main__":
    img=cv.imread("241608262000449.jpg")
    n,stats=picture_pdf_detect(img)
    print(n)