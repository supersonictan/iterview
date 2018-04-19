# -*- coding=utf-8 -*-
#! /usr/bin/env python
import numpy as np

# 创建矩阵
arr = np.array([[1, 2, 3], [2, 3, 4]], dtype=np.float32)
# 创建全零矩阵
z = np.zeros((4, 4), dtype=np.float32)  # one = np.ones((2, 2))  np.empty((3,4))
# 指定步长、起始、结束位置，生成矩3*4阵
a = np.arange(1, 24, 2).reshape((3, 4))
# 指定个数、起止位置，自动匹配步长
b = np.linspace(1, 10, 12).reshape((4, 3))
# 随机 0~1 生成 3*4 矩阵
c = np.random.random((2, 4))
# 每行/列 求 min、max、sum、mean、median(axis=0是列)

# 加法/ 矩阵每个元素平方/ 每个元素cos/ 哪个元素小于10 a < 10/ 矩阵相乘 a.dot(b)/ 矩阵转置/ clip功能

# 上下合并 np.vstack(a,b)
# 左右合并 np.hstack(a,b)
# 多合并 np.concatenate(A,B,C, axis=0)
# 创建新维度 A[:, np.newaxis]
e = np.arange(10)
e = e[:, np.newaxis]
print(e)
#print(a < 10)



d = np.transpose(c)
print(c)
print(d)
print('----')
print(np.nancumprod(c))
print('=====')
print(np.max(c, axis=1))
# print(b)
# print(a)
# print(arr.shape)
# print(arr.ndim)
# print(arr.size)