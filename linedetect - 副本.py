# -*- coding: utf-8 -*-
# @Time    : 2021/3/5
# @Author  : jhh
# @File    : linedetect.py
# @Software: PyCharm
import cv2 as cv
import numpy as np


def line_detection(image):  # 直线检测
    gray_img = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    im_h, im_w = gray_img.shape[:2]
    sobel_img = cv.Sobel(gray_img, cv.CV_8U, 1, 0, ksize=5)
    dst_img = cv.bitwise_not(sobel_img, gray_img)
    # kernel=cv.getStructuringElement(cv.MORPH_RECT,(15,5))
    # dilate_img=cv.morphologyEx(gray_img,cv.MORPH_DILATE,kernel)
    # cv.imshow('dst_img', dst_img)
    # cv.waitKey(0)

    binary_img = cv.adaptiveThreshold(dst_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 11)
    bilateral_img = cv.bilateralFilter(binary_img, 50, 30, 30)
    edges = cv.Canny(bilateral_img, 50, 150, apertureSize=3)  # apertureSize是sobel算子窗口大小
    cv.imshow('edges', edges)
    cv.waitKey(0)
    lines = cv.HoughLines(edges, 1, np.pi / 180, int(im_w / 2))  # 指定步长为1的半径和步长为π/180的角来搜索所有可能的直线

    for line in lines:
        #  print(type(lines))
        rho, theta = line[0]  # 获取极值ρ长度和θ角度
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho  # 获取x轴值
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))  # 获取这条直线最大值点x1
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))  # 获取这条直线最小值点y2　　其中*1000是内部规则
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 划线
        print('x1', x1)

    cv.imshow("image-lines", image)

    #                 font = cv.FONT_HERSHEY_SIMPLEX  # 定义字体
    #                 imgzi = cv.putText(image, str(1), (x1, 50), font, 0.5, (0, 0, 255), 1)
    #                 """
    #                 cv2.putText(src, text, place, Font, Font_Size, Font_Color, Font_Overstriking)
    #                 src	输入图像
    #                 text	需要添加的文字
    #                 place	左上角坐标
    #                 Font	字体类型
    #                 Font_Size	字体大小
    #                 Font_Color	文字颜色
    #                 Font_Overstriking	字体粗细

    """
    HoughLines(image, rho, theta, threshold, lines=None, srn=None, stn=None, min_theta=None, max_theta=None)
    第一个参数image：是canny边缘检测后的图像
    
    第二个参数rho和第三个参数theta：对应直线搜索的步长。在本例中，函数将通过步长为1的半径和步长为π/180的角来搜索所有可能的直线。
    
    最后一个参数threshold：是经过某一点曲线的数量的阈值，超过这个阈值，就表示这个交点所代表的参数对(rho, theta)在原图像中为一条直线

    """


def line_detect_possible_demo(image):
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
    for i, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        x_list.append(x1)
    x_list = np.array(x_list)
    order = np.argsort(x_list, axis=0)
    x_list=x_list[order]
    lines = lines[order]
    for i, line in enumerate(lines):
        x1, y1, x2, y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
        font = cv.FONT_HERSHEY_SIMPLEX  # 定义字体
        imgzi = cv.putText(image, str(i + 1), (x1, 50), font, 0.5, (0, 0, 255), 1)
        print('x1', x1)
    cv.imshow("line_detect_possible_demo", image)
    cv.waitKey(0)


if __name__ == '__main__':
    src = cv.imread("paper_0_0_1.png")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    # line_detection(src)
    line_detect_possible_demo(src)
    cv.waitKey(0)
    cv.destroyAllWindows()
