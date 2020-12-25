# -*- coding: utf-8 -*-
# @Time    : 2020/12/19
# @Author  : jhf
# @File    : testtt.py
# @Software: PyCharm

import numpy as np
z = np.array([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]])
z1=np.reshape(z,(-1,))
print(z.shape)
z2=np.reshape(z1,(4,4))
print(z2)