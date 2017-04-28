#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#将列表转为numpy的数组,指定类型
array = np.array([[1,2,3],[2,3,4]], dtype=np.float)
zero_arr = np.ones((3,4))       #生成为0的矩阵
print (array.dtype)
print("Dim:",array.ndim)        #维度
print('Shape:', array.shape)    #几行几列
print('Size:', array.size)      #元素个数
matrix = np.arange(1,13).reshape((3,4))  #重新定义长宽
matrix.flatten()                     #将矩阵转为列表

#------------------运算------
#加减乘除次方
a = np.array([10,20,30,40])
b = np.arange(1,5)

#矩阵乘法
np.dot(a,b)
a.dot(b)
c = np.random.random((2,4))
#矩阵加和, axis=0在列中运算，axis=1在行中运算
np.sum(c,axis=1)




#矩阵最小/最大
np.min(a)
#矩阵最小值的索引
A = np.arange(2,14).reshape((3,4))
print A
A[1][0]  #行列索引
A[1,:]    #第2行所有的列
for row in A.T: #遍历矩阵
    print row

np.argmax(A)
np.average(A)
np.median(A)
np.cumsum(A)
np.transpose(A)

print "================合并"
Matrix_A = np.array([1,1,1])
Matrix_B = np.array([2,2,2])
np.vstack((Matrix_A,Matrix_B)) #将B添加在A下面
np.hstack((Matrix_A,Matrix_B))  #将A添加在B后面
print C.shape