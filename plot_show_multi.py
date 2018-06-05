# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


# 加载原图,彩色的，默认是BGR
img=cv.imread("imgs/22.png")

#  用于存储所有弹框的图片集合
psw=[]

# 转成RGB模式，否则plot不能正常识别
color_img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

# 放入集合
psw.append(("BGR_SHOW",img))
psw.append(("RGB_SHOW",color_img))



# 获取个数
plot_number=len(psw)


# 设置每列显示的窗体个数
cols=2
# 行数自动推算
rows=plot_number/cols+1


# 打印所有的图片
for index in range(plot_number):
    plt.subplot(rows, cols, index + 1)
    plt.imshow(psw[index][1], cmap = "gray")
    plt.title(psw[index][0], fontsize=8)
    plt.xticks([]), plt.yticks([])  # 隐藏坐标轴

plt.show()




