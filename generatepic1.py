##合成图片
import cv2 as cv
import os
import numpy as np
img_array=[]

##公式和汉字
img_array1=[]
img_array2=[]
file_pathname1=(r'D:\pycharm\work\newdata')#公式
file_pathname2=(r'D:\pycharm\work\hanzi')##文本
for file in os.listdir(file_pathname1):
    img = cv.imread(file_pathname1 + '/' + file)
    img_array1.append(img)

print(img_array1[2].shape)
cv.imshow('1',img_array1[223])
cv.waitKey(0)
for file1 in os.listdir(file_pathname2):
    img1 = cv.imread(file_pathname2 + '/' + file1)
    img_array2.append(img1)
cv.imshow('2',img_array2[223])
cv.waitKey(0)
h=[]
w=[]

h_n=[]
w_n=[]
img_new_array=[]
img_generate_array=[]
print(img_array2[1].shape)#文本
print(img_array1[1].shape)#公式
for i in range(0,224):
    print(img_array2[i].shape)
    # for j in range(0,224):
    h1, w1,_ = img_array1[i].shape
    h.append(h1)
    w.append(w1)
    # print(h[0],w[0])
    h2, w2,_ = img_array2[0].shape
    # h_n.append(h2)
    # w_n .append(w2)

    img1_new=cv.resize(img_array1[i],(w[i],h2))

    img_new_array.append(img1_new)

    img_generate=np.hstack((img_array2[0],img_new_array[i]))
    img_generate_array.append(img_generate)
    # cv.imwrite(r'D:\pycharm\work\rh/%d.png' % (a), img_generate, [int(cv.IMWRITE_JPEG_QUALITY), 95])



print(img_new_array[0].shape)
print(img_array2[0].shape)
print(len(img_generate_array))
img_generate1=np.hstack((img_array2[0],img_new_array[0]))
cv.imshow('0',img_generate1)
cv.waitKey(0)

cv.imwrite(r'D:\pycharm\work\rh/%d.png'%(0), img_generate1, [int( cv.IMWRITE_JPEG_QUALITY), 95])

# print(224*224)