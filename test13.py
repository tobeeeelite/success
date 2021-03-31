# import cv2 as cv
#
# img_path = "1608262000449.jpg"
# img = cv.imread(img_path)
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh1 = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)
# cv.imshow('jt1', thresh1)
# cv.waitKey(0)
import cv2
import matplotlib.pyplot as plt
import numpy as np


def morphological_operators(img, k):
    # Conversion to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binarization
    # IMPORTANT: THRESH_BINARY_INV or THRESH_BINARY can be both used. It depends on the image
    r, th = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    methods = ['erosion', 'dilation', 'gradient']

    kernel = np.ones(k, np.uint8)

    # erosion: shrink image reg
    erosion = cv2.erode(th, kernel, iterations=1)

    # dilation: grow image regions
    dilation = cv2.dilate(th, kernel, iterations=1)

    # Difference between dilation and erosion of an image.
    gradient = cv2.morphologyEx(th, cv2.MORPH_GRADIENT, kernel)

    images = [erosion, dilation, gradient]

    for i in range(3):
        plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(methods[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


def image_blurring(img, k):
    methods = ['Averaging', 'Gaussian', 'Median', 'Bilateral']

    # Average: convolving the image with a normalized box filter
    average_blurred = cv2.blur(img, k)

    # Gaussian: Blurring the image with a gaussian kernel
    gaussian_blurred = cv2.GaussianBlur(img, k, 10, 10)

    # Median: takes median value of the all elements if a filter and
    # replace it with the center pixel
    median_blurred = cv2.medianBlur(img, k[0])

    # Bilateral: highly effective at noise removal while preserving edges
    bilateral_blurred = cv2.bilateralFilter(img, 10, 75, 75)

    images = [average_blurred, gaussian_blurred, median_blurred, bilateral_blurred]

    for i in range(4):

        # plt.imshow(images[i], 'gray')
        #
        # plt.title(methods[i])
        # plt.xticks([]), plt.yticks([])
        #
        # plt.show()
        img_name='.png'
        plt.imsave(str(i)+img_name,images[i])


def image_gradient(img, k):
    # Image smoothing and differentiation

    methods = ['sobelx', 'sobely', 'laplacian']

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, k)

    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, k)

    laplacian = cv2.Laplacian(img, cv2.CV_64F)

    images = [sobelx, sobely, laplacian]

    for i in range(3):
        plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(methods[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


def increase_brightness(gamma, img):
    # Gamma values specify the brightness factor of an image
    effected_image = np.power(img, gamma)

    plt.imshow(effected_image)

    plt.show()

    return effected_image


def contrast(img):
    # increases the contrast of an image
    timg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Convert to HSV colorspace
    hsv = cv2.cvtColor(timg, cv2.COLOR_BGR2HSV)
    # hsv
    hsv[:, :, 2] = cv2.equalizeHist(hsv[:, :, 2])
    fimg = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

    plt.imshow(fimg)
    plt.show()

    return fimg
if __name__ == '__main__':
    img = cv2.imread(r'E:\work\segmentation\origin\1.png')
    # Important note: You can change parameters and try functions one by one
    # .                to see the results

    # morphological_operators(img, 5)
    image_blurring(img,(5,5))
    # image_gradient(img,5)
    # increase_brightness(2,img)
    # contrast(img)