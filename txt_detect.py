# -*- coding: utf-8 -*-
# @Time    : 2021/3/8
# @Author  : jhh
# @File    : txt_detect.py
# @Software: PyCharm
import cv2 as cv
import numpy as np

"""
1、通过水平投影对图形进行水平分割，获取每一行的图像；

2、通过垂直投影对分割的每一行图像进行垂直分割，最终确定每一个字符的坐标位置，分割出每一个字符；

 　　先简单介绍一下投影法：分别在水平和垂直方向对预处理（二值化）的图像某一种像素进行统计，对于二值化图像非黑即白，我们通过对其中的白点或者黑点进行统计，根据统计结果就可以判断出每一行的上下边界以及每一列的左右边界，从而实现分割的目的。
"""


def line_detect(image):
    gray_img = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    im_h, im_w = gray_img.shape[:2]
    sobel_img = cv.Sobel(gray_img, cv.CV_8U, 1, 0, ksize=5)
    dst_img = cv.bitwise_not(sobel_img, gray_img)
    binary_img = cv.adaptiveThreshold(dst_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 11)
    bilateral_img = cv.bilateralFilter(binary_img, 50, 30, 30)
    edges = cv.Canny(bilateral_img, 50, 150, apertureSize=3)  # apertureSize是sobel算子窗口大小
    lines = cv.HoughLinesP(edges, 1, np.pi / 2, int(im_w / 2), minLineLength=int(0.7 * im_h), maxLineGap=20)
    lines = np.array(lines)
    # lines_list=lines.tolist()
    x_list = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        x_list.append(x1)
    x_list = np.array(x_list)
    order = np.argsort(x_list, axis=0)
    x_list = x_list[order]
    lines = lines[order]
    img_list = []
    a = len(x_list)
    x_delete_list = []
    for i in range(len(x_list)):
        if i == 0:

            img_list.append(image[:, 0:x_list[i], :])
        elif i + 1 <= len(x_list):
            if x_list[i] - x_list[i - 1] < 0.1 * im_w:
                x_delete_list.append(x_list[i - 1])
                continue
            else:
                img_list.append(image[:, x_list[i - 1]:x_list[i], :])
    img_list.append(image[:, x_list[a - 1]:, :])
    x_list = x_list.tolist()
    for x in x_delete_list:
        x_list.remove(x)
    img_w_list = []
    img_list_delete = []

    for j in range(len(img_list)):
        _, img_w = img_list[j].shape[:2]
        img_w_list.append(img_w)
        if img_w_list[j] < 0.1 * im_w:
            img_list_delete.append(img_list[j])
        else:
            continue

    for imag in img_list_delete:
        img_list.remove(imag)

    # for k in range(len(img_list)):
    #     img_name = str(k)
    #     cv.imshow(img_name, img_list[k])
    #     cv.waitKey(0)

    # for i, line in enumerate(lines):
    #     x1, y1, x2, y2 = line[0]
    #     cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
    #     font = cv.FONT_HERSHEY_SIMPLEX  # 定义字体
    #     imgzi = cv.putText(image, str(i + 1), (x1, 50), font, 0.5, (0, 0, 255), 1)
    #     print('x1', x1)
    # cv.imshow("line_detect_possible_demo", image)
    # cv.waitKey(0)
    return img_list, x_list


def get_hprojection(img):
    # hProjection = np.zeros(img.shape, np.uint8)

    im_h, im_w = img.shape[:2]
    h_list = [0 for z in range(0, im_h)]
    img = np.array(img)
    a = np.sum(img, axis=1)
    idx = np.where(img == 0)

    a_list = []

    for i in range(0, im_h):
        for j in range(0, im_w):
            if img[i, j] == 0:
                h_list[i] += 1
            else:
                continue
    for i, h in enumerate(h_list):
        if h < 10:
            h_list[i] = 0
        else:
            continue
    idx_list = []
    for idx, h in enumerate(h_list):
        if h != 0:
            idx_list.append(idx)
    idx_remain = []
    for j in range(len(idx_list)):
        if j == 0:
            if idx_list[j + 1] - idx_list[0] > 1:
                idx_remain.append(idx_list[0])
                idx_remain.append(idx_list[j + 1])
            else:
                idx_remain.append(idx_list[0])
        elif j + 1 <= (len(idx_list) - 1):

            if idx_list[j + 1] - idx_list[j] > 1:

                idx_remain.append(idx_list[j])
                idx_remain.append(idx_list[j + 1])
            else:
                continue

    img_white = np.ones(shape=(im_h, im_w), dtype=np.uint8) * 255
    # for i in range(im_h):
    #     pt1 = (im_w - 1, i)
    #     pt2 = (im_w - 1 - h_list[i], i)
    #     cv.line(img_white, pt1, pt2, (0,), 1)
    # cv.imshow('水平投影', img_white)
    # cv.waitKey(0)

    # cv.imshow('img11', img[285:361, 2:])
    # cv.waitKey(0)
    return idx_remain


def get_vprojection(img):
    vProjection = np.zeros(img.shape, np.uint8)
    # 图像高与宽
    im_h, im_w = img.shape[:2]
    # 长度与图像宽度一致的数组
    w_list = [0 for z in range(0, im_w)]
    # 循环统计每一列白色像素的个数
    for i in range(im_w):
        for j in range(im_h):
            if img[j, i] == 255:
                w_list[i] += 1
    for i, w in enumerate(w_list):
        if w < 10:
            w_list[i] = 0
        else:
            continue
    idx_list = []
    for idx, w in enumerate(w_list):
        if w != 0:
            idx_list.append(idx)
    idx_remain = []
    for j in range(len(idx_list)):
        if j == 0:
            if idx_list[j + 1] - idx_list[0] > 1:
                idx_remain.append(idx_list[0])
                idx_remain.append(idx_list[j + 1])
            else:
                idx_remain.append(idx_list[0])
        elif j + 1 <= (len(idx_list) - 1):

            if idx_list[j + 1] - idx_list[j] > 1:

                idx_remain.append(idx_list[j])
                idx_remain.append(idx_list[j + 1])
            else:
                continue
    # 绘制垂直平投影图像
    # for i in range(im_w):
    #     for j in range(im_h - w_list[i], im_h):
    #         vProjection[j, i] = 255
    # cv.imshow('vProjection', vProjection)
    # cv.waitKey(0)
    return w_list


if __name__ == '__main__':
    img_path = "paper_0_0.png"
    image = cv.imread(img_path)
    img_list, x_list = line_detect(image)
    # 图像灰度化
    idx_remain_list = []

    for j in range(len(img_list)):
        gray_img = cv.cvtColor(img_list[j], cv.COLOR_RGB2GRAY)
        # img = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 35, 25)
        # gray_img = []
        _, img = cv.threshold(gray_img, 0, 255, cv.THRESH_OTSU + cv.THRESH_BINARY)
        gray_img=[]

        img = cv.bilateralFilter(img, 50, 30, 30)

        # cv.imshow('img0', img)
        # cv.waitKey(0)
        # im_h, im_w = img_list[j].shape[:2]
        # 图像高与宽

        # get_vprojection(img)
        # get_vprojection(img)

        # 水平投影
        idx_remain = get_hprojection(img)
        idx_remain_list.append(idx_remain)
        img = []
        ##先将页面切分开
        for i in range(len(idx_remain_list[j])):
            if i + 1 <= len(idx_remain_list[j]) - 1:
                # img_name = str(i)
                if idx_remain_list[j][i] == idx_remain_list[j][i + 1]:
                    continue
                elif idx_remain_list[j][i + 1] - idx_remain_list[j][i] < 6:
                    continue
                else:
                    if j == 0:
                        if x_list[j] < 0.1 * image.shape[1]:
                            cv.rectangle(image, (x_list[j]+5, idx_remain_list[j][i]),
                                         (x_list[j + 1], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
                        elif x_list[j] > 0.3 * image.shape[1]:
                            cv.rectangle(image, (0, idx_remain_list[j][i]),
                                         (x_list[j], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
                    else:
                        if len(x_list) == 1:
                            cv.rectangle(image, (x_list[0], idx_remain_list[j][i]),
                                         (image.shape[1], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
                        else:
                            if x_list[len(x_list) - 1] > 0.8 * image.shape[1]:
                                cv.rectangle(image, (x_list[j - 1], idx_remain_list[j][i]),
                                             (x_list[j], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
                            else:
                                if j + 1 < len(x_list):
                                    cv.rectangle(image, (x_list[j], idx_remain_list[j][i]),
                                                 (x_list[j + 1], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
                                else:
                                    cv.rectangle(image, (x_list[j], idx_remain_list[j][i]),
                                                 (image.shape[1], idx_remain_list[j][i + 1]), (0, 0, 255), 1)
            else:
                break

    cv.imshow('image', image)
    cv.waitKey(0)
