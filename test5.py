# import matplotlib.pyplot as plt
# import pylab as pl
#
# x = range(10) # 横轴的数据
# y = [i*i for i in x] # 纵轴的数据
# pl.plot(x, y) # 调用pylab的plot函数绘制曲线
# pl.show() # 显示绘制出的图
# import matplotlib.pyplot as plt  # plt 用于显示图片
# import matplotlib.image as mpimg  # mpimg 用于读取图片
# import numpy as np
#
# lena = mpimg.imread('000.png')  # 读取和代码处于同一目录下的 lena.png
# # 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
# lena.shape  # (512, 512, 3)
#
# plt.imshow(lena)  # 显示图片
# plt.axis('off')  # 不显示坐标轴
# plt.show()

# !/usr/bin/env python
# -*-coding : utf-8-*-

import sys
from PIL import Image

def epsfn(fn):
    if fn:
        i = fn.rfind('.')
        return fn[:i] + '.eps'
    return None


def convert2eps(fn, eps):
    im = Image.open(fn)
    im.save(eps)


if __name__ == '__main__':
    i = 0
    fn = r'1.jpg'
    # for fn in sys.argv[1:]:
    eps = epsfn(fn)
    print('conv %s to %s' % (fn, eps))
    convert2eps(fn, eps)

    print('Convert %s/%s images.\nDone!\n' % (i, len(sys.argv[1:])))
