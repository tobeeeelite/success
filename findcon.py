
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21
# @Author  : jhf
# @File    : contour_extraction.py
# @Software: PyCharm
import cv2
import numpy as np

def contour_extraction(img, bf, max_width, max_height):
    # Image shape
    height, width, dim = img.shape

    # gray-scale of the image
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # To reduce the noise, I used gaussian blur technique
    blur = cv2.GaussianBlur(img_gray, (bf, bf), 3)

    # Conversion from gray to binary
    r, th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Eroding enables to divide objects from each other
    kernel = np.ones((3, 3), np.uint8)
    eroded = cv2.erode(th, kernel, iterations=1)

    # Contour extraction of the image
    contours, hierarchy = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    template = np.zeros((height, width), np.uint8)
    margin = 6
    newimg = []

    for i, cont in enumerate(contours):

        # Extracting every object contour
        x, y, w, h = cv2.boundingRect(cont)

        # Upper and lower boundaries of the object
        if 3 < w < max_width and 3 < h < max_height:

            newimg = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # margin is used with two ways.
            # 1. if the object is so close to the edge of the image, it extracts
            #  only the contour region
            # 2. Otherwise, the object can be extracted by creating some gaps (-2) from
            # the contours to each direction

            if x < margin or y < margin or y > height - margin or x > width - margin:

                letter_image = img[y:y + h, x:x + w]
                image_name = 'extracted_original' + str(i) + '.jpg'
                cv2.imwrite(image_name, letter_image)

            else:

                letter_image = img[y - 2:y + h + 2, x - 2:x + w + 2]
                image_name = 'extracted_original' + str(i) + '.jpg'
                cv2.imwrite(image_name, letter_image)

    return newimg


if __name__ == '__main__':
    img = cv2.imread('0.jpg')
    finalimg = contour_extraction(img, 3, 150, 150)

    cv2.imshow('centered_image', finalimg)
    cv2.waitKey()

