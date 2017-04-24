#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

#将列表转为numpy的数组
array = np.array([[1,2,3],[2,3,4]], dtype=np.float)
zero_arr = np.ones((3,4))       #生成为0的矩阵
print (array.dtype)
print("Dim:",array.ndim)        #维度
print('Shape:', array.shape)    #几行几列
print('Size:', array.size)      #元素个数
np.arange(1,13).reshape((3,4))  #重新定义长宽

#------------------运算------
#加减乘除次方
a = np.array([10,20,30,40])
b = np.arange(1,5)

#矩阵乘法
np.dot(a,b)
a.dot(b)

c = np.random.random((2,4))
print c
#矩阵加和, axis=0在列中运算，axis=1在行中运算
print (np.sum(c,axis=1))
#矩阵最小/最大
np.min(a)
#矩阵最小值的索引
A = np.arange(2,14).reshape((3,4))
np.argmax(A)
np.average(A)
np.median(A)
np.cumsum(A)
np.transpose(A)