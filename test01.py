import cv2 as cv
import numpy as np
from scipy import stats
import copy

def correct_img(img0, location):
    points = np.zeros((4, 2))
    points[:, 0] = location[:, 1]
    points[:, 1] = location[:, 0]
    x1, y1, x2, y2 = np.min(points[:, 0]), np.min(points[:, 1]), np.max(points[:, 0]), np.max(points[:, 1])
    width = int(x2 - x1)  ##向下取整
    height = int(y2 - y1)
    dst = [[width, 0], [0, 0], [0, height], [width, height]]
    ##透射变换
    ##.astype 数据类型变换
    M = cv.getPerspectiveTransform(points.astype(np.float32), np.asarray(dst, dtype=np.float32))
    temp_img = cv.warpPerspective(img0, M, (width, height))
    return temp_img


def img_enhance01(img):
    ##图像增强
    v = [5.2159834956623136e-09, -2.957228911442498e-06, 0.0005162834373579167, -0.027038011262549483,
         1.3039165483670454, -0.030121790711686906]  # 012345
    ##多项式
    f = np.poly1d(np.asarray(v))
    lut = []
    for i in range(256):
        t = int(f(i))
        if t < 0:
            t = 0
        if t > 255:
            t = 255
        lut.append(t)
        ##函数主要是用来起到突出的有用信息，增强图像的光对比度的作用。通过对input的灰度像素的改变，可以通过映射的关系得到需要输出的灰度像素矩阵output
    lut_img = cv.LUT(img, np.asarray(lut, np.uint8))
    ##np.asarray 将输入转为矩阵格式
    return lut_img


def get_sorted_connected_components(img0):
    hh, ww = img0.shape[:2]
    ##连通区域 nn是连通区域的数目 temp_label图像上每一像素的标记，用数字1、2、3…表示（不同的数字表示不同的连通域）
    nn, temp_label = cv.connectedComponents(img0, connectivity=8)  # 8连通
    region_list = []
    for i in range(nn):
        y, x = np.where(temp_label == i)
        point = np.asarray([y, x])
        rect = cv.minAreaRect(point.T)  ##最小外接矩 # 得到最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
        box = cv.boxPoints(rect)  # cv2.boxPoints(rect) for OpenCV 3.x 获取最小外接矩形的4个顶点
        x1 = np.min(box[:, 1])
        y1 = np.min(box[:, 0])
        x2 = np.max(box[:, 1])
        y2 = np.max(box[:, 0])
        if y1 < 0:
            y1 = 0
        if x1 < 0:
            x1 = 0
        h = y2 - y1
        if h > 0.5 * hh:
            continue
        region_list.append(np.r_[rect[0], np.asarray([y1, x1, y2, x2])])  # np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。
    connect_components = np.asarray(region_list)
    connect_components = connect_components[np.argsort(connect_components[:, 0])]#argsort()是将X中的元素从小到大排序后，提取对应的索引index，然后输出到y
    return connect_components


def recognition_fill_region(option_region, fill_region, options=4, include_qid=False):
    s1 = option_region[1]
    e1 = option_region[3]
    if include_qid:
        options += 1
    d = (e1 - s1) / options
    ans = int((fill_region[1] - s1) / d)
    return ans

##step1
def answerSheetDetect(img):
    img_h, img_w = img.shape[:2]
    new_img_h, new_img_w = int(img_h / 2), int(img_w / 2)
    new_img = cv.resize(img, (new_img_w, new_img_h))
    gray_img = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)##转换成为灰度图像
    blur_img = cv.blur(gray_img, (5, 5))##平滑滤波
    ##图像的二值化
    th, binary_img = cv.threshold(blur_img, 127, 255, cv.THRESH_OTSU)#THRESH_OTSU不支持32位
    laplacian_img = cv.Laplacian(binary_img, -1)
    n, labels = cv.connectedComponents(laplacian_img)
    blank_img = np.ones_like(new_img, dtype=np.uint8) * 255  ##返回一个用1填充的跟输入 形状和类型 一致的数组。
    area_th = 0.6 * new_img_w * new_img_h
    box = None
    for i in range(n):
        y, x = np.where(labels == i)
        x1 = np.min(x)
        y1 = np.min(y)
        x2 = np.max(x)
        y2 = np.max(y)
        if (x2 - x1 > 0.95 * new_img_w or y2 - y1 > 0.95 * new_img_h):
            continue
        if ((x2 - x1) * (y2 - y1) > 0.6 * area_th):
            point = np.asarray([y, x])
            rect = cv.minAreaRect(point.T)
            box = cv.boxPoints(rect)
            blank_img[y, x] = np.random.randint(0, 255, (3))
    box *= 2
    ##矫正图片
    temp_img = correct_img(img, box)
    dst_img = cv.transpose(temp_img)
    dst_img = cv.flip(dst_img, 1)
    enhance_img = img_enhance01(dst_img)
    return enhance_img

##定位目标框
def optionRegionDetect(img):
    img_h, img_w = img.shape[:2]
    new_img_h, new_img_w = int(img_h), int(img_w)
    print(new_img_h, new_img_w)
    new_img = cv.resize(img, (new_img_w, new_img_h))
    gray_img = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
    ##腐蚀操作
    horizontalKernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 5))
    horImg = cv.morphologyEx(gray_img, cv.MORPH_ERODE, horizontalKernel)
    cv.imshow('horImg',horImg)
    cv.waitKey(0)
    ##二值化图像
    th, binary_img = cv.threshold(horImg, 127, 255, cv.THRESH_OTSU)
    fill_img = np.ones_like(new_img, dtype=np.uint8) * 255
    n, labels = cv.connectedComponents(binary_img, connectivity=8)
    cv.imshow('bb',binary_img)
    cv.waitKey(0)
    print(n)
    for i in range(n):
        if i==0:
            continue
        y, x = np.where(labels == i)
        point = np.asarray([y, x])

        rect = cv.minAreaRect(point.T)
        box = cv.boxPoints(rect)

        x1 = np.min(box[:, 1])
        y1 = np.min(box[:, 0])
        x2 = np.max(box[:, 1])
        y2 = np.max(box[:, 0])
        if y2 - y1 > 0.8 * new_img_h or y2 - y1 < 0.2 * new_img_h:
            continue
        if x2 - x1 > 0.5 * new_img_w:
            fill_img[y, x] = np.random.randint(0, 256, 3)
            return [int(x1), int(y1), int(x2 - x1), int(y2 - y1)]
    # cv.namedWindow("white_img", cv.WINDOW_NORMAL)
    # cv.imshow("white_img", fill_img)
    # cv.waitKey(0)
    return None


def recognition(img, rect):
    sub_img = img[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
    img_h, img_w = sub_img.shape[:2]
    print(img_h,img_w)
    gray_img = cv.cvtColor(sub_img, cv.COLOR_BGR2GRAY)
    th, binary_img = cv.threshold(gray_img, 127, 255, cv.THRESH_OTSU)#返回一个随机整型数，范围从低（包括）到高（不包括），即[low, high)
    # binary_img = cv.adaptiveThreshold(gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 21)
    ##开运算 先腐蚀后膨胀

    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    morp_img1 = cv.morphologyEx(binary_img, cv.MORPH_OPEN, kernel)
    binary_img2 = cv.bitwise_not(morp_img1)#bitwise_not是对二进制数据进行“非”操作，即对图像（灰度图像或彩色图像均可）每个像素值进行二进制“非”操作，~1=0，~0=1
    n, lables = cv.connectedComponents(binary_img2, connectivity=8)
    print("连通域：", n)

    w_list = []
    h_list = []
    for i in range(n):
        if i==0:
            continue
        y, x = np.where(lables == i)
        point = np.asarray([y, x])
        rect = cv.minAreaRect(point.T)
        box = cv.boxPoints(rect)
        x1 = np.min(box[:, 1])
        y1 = np.min(box[:, 0])
        x2 = np.max(box[:, 1])
        y2 = np.max(box[:, 0])
        w = x2 - x1
        h = y2 - y1
        # w_list.append(w)
        # h_list.append(h)
        if w < 100 and h < 100:
            w_list.append(w)
            h_list.append(h)
        else:
            continue
    ww = stats.mode(w_list)[0][0]##用scipy.stats.mode函数寻找数组或者矩阵每行/每列中最常出现成员以及出现的次数
    hh = stats.mode(h_list)[0][0]
    ##统计每一个选项的宽高

    print(len(h_list))
    print(ww)
    print(hh)

    area = ww * hh
    morp_img2 = copy.deepcopy(morp_img1)##一旦复制出来了，就是独立的

    fill_region = {}
    count = 0
    tt = np.ones_like(sub_img, dtype=np.uint8) * 255
    for i in range(n):
        y, x = np.where(lables == i)
        l = len(x)
        point = np.asarray([y, x])##转成矩阵
        rect = cv.minAreaRect(point.T)
        box = cv.boxPoints(rect)
        x1 = np.min(box[:, 1])
        y1 = np.min(box[:, 0])
        x2 = np.max(box[:, 1])
        y2 = np.max(box[:, 0])
        w = x2 - x1
        h = y2 - y1
        coverage = l / area
        if w < 0.7 * ww:
            morp_img2[y, x] = 255
        if w > 700:
            morp_img2[y, x] = 255
            continue
        if coverage > 0.8:
            tt[y, x] = count
            # tt[y, x] = np.random.randint(0, 255, (3,))
            fill_region[count] = np.asarray([rect[0][0], rect[0][1], coverage])
            count += 1
    ##开闭运算
    ##把题号去掉
    cv.namedWindow('1',cv.WINDOW_NORMAL)
    cv.imshow("morp_img1", morp_img1)
    cv.imshow('1',morp_img2)
    cv.waitKey(0)
    kernel_2 = cv.getStructuringElement(cv.MORPH_RECT, (20, 1))
    morp_img3 = cv.morphologyEx(morp_img2, cv.MORPH_OPEN, kernel_2)

    kernel3 = cv.getStructuringElement(cv.MORPH_RECT, (4, 20))
    mrop_img4 = cv.morphologyEx(morp_img3, cv.MORPH_OPEN, kernel3)
    kernel4 = cv.getStructuringElement(cv.MORPH_RECT, (10, 1))
    mrop_img4 = cv.morphologyEx(mrop_img4, cv.MORPH_CLOSE, kernel4)

    n2, labels2 = cv.connectedComponents(cv.bitwise_not(mrop_img4), connectivity=8)
    print(n2)
    tt2 = np.ones_like(sub_img, dtype=np.uint8) * 255
    center_list = []
    area_th = 0.01 * img_w * img_h
    aver_height = 0
    for i in range(n2):
        y, x = np.where(labels2 == i)
        l = len(x)
        print(len(y))
        point = np.asarray([y, x])
        rect = cv.minAreaRect(point.T)
        box = cv.boxPoints(rect)
        x1 = np.min(box[:, 1])
        y1 = np.min(box[:, 0])
        x2 = np.max(box[:, 1])
        y2 = np.max(box[:, 0])
        if y1 < 0:
            y1 = 0
        w = x2 - x1
        h = y2 - y1
        if w > 0.5 * img_w or h > 0.5 * img_h:
            continue
        if l > 0.6 * w * h and l > area_th:
            # tt2[y, x] =  np.random.randint(0, 255, (3,))
            center_list.append(np.r_[rect[0], np.asarray([y1, x1, y2, x2])])
            aver_height += y2 - y1
    aver_height = aver_height / len(center_list)
    point_mat = np.asarray(center_list)
    point_mat = point_mat[np.argsort(point_mat[:, 0])]
    s = 0
    region_list = []
    for i in range(point_mat.shape[0]):
        if i == 0:
            continue
        pre_center = point_mat[i - 1]
        center = point_mat[i]
        interval_w = np.abs(center[1] - pre_center[1])
        interval_h = np.abs(center[0] - pre_center[0])
        if interval_h > 0.6 * aver_height:
            new_region = point_mat[s:i]
            new_region = new_region[np.argsort(new_region[:, 1])]
            region_list.append(new_region)
            s = i
    new_region = point_mat[s:]
    new_region = new_region[np.argsort(new_region[:, 1])]
    region_list.append(new_region)
    binary_mrop_img2_inverse = cv.bitwise_not(morp_img3)
    cv.namedWindow('morp_img44', cv.WINDOW_NORMAL)
    cv.imshow('morp_img44', binary_mrop_img2_inverse)
    cv.waitKey(0)
    region_ind = 0
    for line_region in region_list:
        for region in line_region:
            yt1, xt1, yt2, xt2 = region[2:].astype(np.int)
            temp_img = binary_mrop_img2_inverse[yt1:yt2, xt1:xt2]
            temp_tt = tt[yt1:yt2, xt1:xt2]
            conn_comp = get_sorted_connected_components(temp_img)
            print("conn_comp", len(conn_comp))
            for ind, comp in enumerate(conn_comp):
                y1, x1, y2, x2 = comp[2:].astype(np.int)
                temp_img2 = temp_tt[y1:y2, x1:x2]
                b = np.unique(temp_img2)
                q_id = region_ind * 5 + ind
                options_t = question_options[q_id]
                for e in b:
                    if e == 255:
                        continue
                    y_t, x_t, coverage_t = fill_region[e]
                    ans = recognition_fill_region([y1 + yt1, x1 + xt1, y2 + yt1, x2 + xt1], [y_t, x_t], options_t,
                                                  include_qid=False)
                    if False:
                        if ans == 0:
                            print(q_id + 1, "题号")
                        else:
                            p = (int(x_t), int(y_t))
                            cv.putText(sub_img, chr(ans + 64), p, cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
                    else:
                        p = (int(x_t), int(y_t))
                        cv.putText(sub_img, chr(ans + 65), p, cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))
                        print(q_id + 1, chr(ans + 65))
            region_ind += 1
    cv.imshow("sub_img", sub_img)
    cv.waitKey(0)


if __name__ == '__main__':
    question_options = np.ones([60]) * 4
    question_options[:20] = 3
    question_options[35:40] = 7
    img_path = r"D:\pycharm\work\scan02(1).jpg"
    img = cv.imread(img_path)
    answerSheetImg = answerSheetDetect(img)
    # cv.imshow("answerSheetImg", answerSheetImg)
    # cv.waitKey(0)
    optionsRect = optionRegionDetect(answerSheetImg)
    print(optionsRect)
    recognition(answerSheetImg, optionsRect)
