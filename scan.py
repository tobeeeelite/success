# -*- coding: utf-8 -*-
# @Time    : 2020/12/22
# @Author  : jhf
# @File    : scan.py
# @Software: PyCharm

import cv2, imutils

import numpy as np
import cv2
from PIL import ImageEnhance

def order_points(pts):
    rect = np.zeros((4, 2), dtype="float32")

    s = np.sum(pts, axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect


def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2)
    widthB = np.sqrt((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2)
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt((tr[0] - br[0]) ** 2 + (tr[1] - br[1]) ** 2)
    heightB = np.sqrt((tl[0] - bl[0]) ** 2 + (tl[1] - bl[1]) ** 2)
    maxHeight = max(int(heightA), int(heightB))

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped




def preProcess(image):
    ratio = image.shape[0] / 500.0
    image = imutils.resize(image, height=500)

    grayImage  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gaussImage = cv2.GaussianBlur(grayImage, (5, 5), 0)
    edgedImage = cv2.Canny(gaussImage, 75, 200)

    cnts = cv2.findContours(edgedImage.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[1] if imutils.is_cv2() else cnts[0]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        peri = cv2.arcLength(c, True)  # Calculating contour circumference
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            screenCnt = approx
            break

    return  screenCnt, ratio


class Enhancer:
    def bright(self, image, brightness):
        enh_bri = ImageEnhance.Brightness(image)
        brightness = brightness
        imageBrightend = enh_bri.enhance(brightness)
        return imageBrightend

    def color(self, image, color):
        enh_col = ImageEnhance.Color(image)
        color = color
        imageColored = enh_col.enhance(color)
        return imageColored

    def contrast(self, image, contrast):
        enh_con = ImageEnhance.Contrast(image)
        contrast = contrast
        image_contrasted = enh_con.enhance(contrast)
        return image_contrasted

    def sharp(self, image, sharpness):
        enh_sha = ImageEnhance.Sharpness(image)
        sharpness = sharpness
        image_sharped = enh_sha.enhance(sharpness)
        return image_sharped

    def gamma(self, image, gamma):
        # gamma_table = [np.power(x / 255.0, gamma) * 255.0 for x in range(256)]
        # gamma_table = np.round(np.array(gamma_table)).astype(np.uint8)
        # return cv2.LUT(image, gamma_table)
        gamma_image = np.power(image / float(np.max(image)), gamma)
        return gamma_image
if __name__ == "__main__":

    image = cv2.imread(r'D:\pycharm\work\enhancepic\0.jpg')
    screenCnt, ratio = preProcess(image)
    warped = four_point_transform(image, screenCnt.reshape(4, 2) * ratio)

    enhancer = imgEnhance.Enhancer()
    enhancedImg = enhancer.gamma(warped,1.63)

    cv2.imshow("org", imutils.resize(image, height=500))
    cv2.imshow("gamma", imutils.resize(enhancedImg, height=500))
    cv2.waitKey(0)
    cv2.destroyAllWindows()