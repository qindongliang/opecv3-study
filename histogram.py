# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

"""
直方图学习例子
"""

img = cv.imread('E:\\tmp\\cat.jpg')

cv.imshow("orgin",img)

def gray_histogram():
    """
    灰度图
    :return:
    """
    # ravel方法代表返回一个连续扁平化的数组
    # hist参数：数组，bin数量，像素值范围
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    plt.hist(gray.ravel(), 256, [0, 256])


def color_histogram():
    """
    彩色图
    :return:
    """
    # 蓝 绿 红
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])


gray_histogram()

# color_histogram()


plt.show()

cv.waitKey(0)