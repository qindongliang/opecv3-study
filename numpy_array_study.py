# -*- coding:utf-8 -*-
import numpy as np



def test1():
    # 通过python的list来构建numpy array
    list1 = [[1, 2, 3]]
    list2 = [[1], [2], [3]]

    # 通过python的 tuple来构造
    tuple3= [(1,2,3)]

    # 使用array方法构造
    nd1 = np.array(list1)
    nd2 = np.array(list2)
    nd3 = np.array(tuple3)

    show_array_properties(nd1)
    show_array_properties(nd2)
    show_array_properties(nd3)





def show_array_properties(np_array):
    print("-----------------------")
    """
    常用属性介绍
    :param np_array: 
    :return: 
    """
    print(np_array.shape) # 代表每一个维度元素的个数
    print(np_array.ndim)  # 总共多少维度
    print(np_array.dtype) # 数据类型
    print(np_array.size) # 数组中元素的个数


# example1
print("================example1")
test1()


# example2
print("================example2")
# 构建一个2维数组
a = np.array([[1,2,3],[3,4,5],[4,5,6]])


print(a[0:3:2])  # start:stop:step

# [[1 2 3]
#  [4 5 6]]



# example3
print("================example3")
b=np.arange(10)

print(b) # [0 1 2 3 4 5 6 7 8 9]

print(b[2]) #   2

b=np.arange(1,6,2)

print(b) # [1 3 5]

# example4
print("================example4")

c=np.arange(10)

print(c[2:]) # [2 3 4 5 6 7 8 9]

# example5
print("================example5")

c=np.arange(10)

print(c[2:5]) # [2 3 4]

# example6
print("================example6")


d = np.array([[1,2,3],[3,4,5],[4,5,6]])

print(d[1:])

# [[3 4 5]
#  [4 5 6]]


# example7
print("================example7")

d = np.array([[1,2,3],[3,4,5],[4,5,6]])

print(d[:,1])  #  [2 4 5]


print(d[1,:]) # [3 4 5]

print(d[:,1:])

# [[2 3]
#  [4 5]
#  [5 6]]


# example8
print("================example8")

e = np.array([[7,2,3],[3,4,5],[4,5,6]])

all_first=e[:,0]

print(all_first) # [7 3 4]

asc_sort_order= np.argsort(all_first)

print(asc_sort_order) #[1 2 0]

left_two= asc_sort_order[:2]

print(left_two) # [1 2]

two_after=asc_sort_order[2:]

print(two_after) # [0]

sort_result= e[asc_sort_order,:]

print(sort_result)

# [[3 4 5]
#  [4 5 6]
#  [7 2 3]]


# example9
print("================example9")

list=[1,2,3,4,5,6,7,8]

array2d=np.array(list)

print(array2d.reshape(4,2))

# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
