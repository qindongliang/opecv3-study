# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv

"""
分别使用opencv和matplot在
同一个窗体中展示多个图片
"""


def opecv_multi_pic():
    # 图1
    img = cv.imread('E:\\tmp\\cat.jpg')
    # 图2
    img2 = cv.imread('E:\\tmp\\cat.jpg')
    # 图集
    imgs = np.hstack([img,img2])

    # 展示多个
    cv.imshow("mutil_pic", imgs)

    #等待关闭
    cv.waitKey(0)




def matplotlib_multi_pic1():
    for i in range(9):
        img = cv.imread('E:\\tmp\\cat.jpg')
        title="title"+str(i+1)
        #行，列，索引
        plt.subplot(3,3,i+1)
        plt.imshow(img)
        plt.title(title,fontsize=8)
        plt.xticks([])
        plt.yticks([])
    plt.show()


def matplotlib_multi_pic2():

        plt.gcf().canvas.set_window_title('Test')
        plt.gcf().suptitle("multi pic test")

        # img = cv.imread('E:\\tmp\\cat.jpg')
        img = cv.imread('E:\\tmp\\cat.jpg')
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        img2 = cv.imread('E:\\tmp\\test6.jpg')
        gray2 = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

        img3 = cv.imread('E:\\tmp\\hough.jpg')


        #如果总图片个数不超过10，我们还可以用快速的方法
        # 321分别代表行，列，索引
        plt.subplot(321),plt.imshow(img),plt.title("321")
        plt.subplot(322),plt.imshow(gray),plt.title("322")
        plt.subplot(323),plt.imshow(img2),plt.title("323")
        plt.subplot(324),plt.imshow(gray2),plt.title("324")
        plt.subplot(326),plt.imshow(img3),plt.title("326")


        plt.show()



# opecv_muti_pic()

# matplotlib_multi_pic1()
# matplotlib_multi_pic2()

