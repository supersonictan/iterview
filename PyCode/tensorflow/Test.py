#!/usr/bin/python
# -*- coding: utf-8 -*-
# import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

"""
创建小图 method 1
"""
# 创建数据集
x = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x.shape)  # 正态分布:均值、标准差、shape
y1 = np.square(x) - 0.5 + noise
y2 = 2* x + 1


plt.figure()

# pic_1
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3, rowspan=1)  # 3行3列, 从0,0开始, 行跨度, 列跨度
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title_1')
ax = plt.gca()  #get current axis
ax.spines['right'].set_color('none')  # 无色: 右边和顶部边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 设置x坐标轴为下边框
ax.yaxis.set_ticks_position('left')  # 设置y坐标轴为左边框
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# pic_2
ax1 = plt.subplot2grid((3,3), (1,0), colspan=1, rowspan=1)  # 3行3列, 从0,0开始, 行跨度, 列跨度
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax = plt.gca()  #get current axis
ax.spines['right'].set_color('none')  # 无色: 右边和顶部边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 设置x坐标轴为下边框
ax.yaxis.set_ticks_position('left')  # 设置y坐标轴为左边框
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# pic_3
ax1 = plt.subplot2grid((3,3), (1,1), colspan=1, rowspan=1)  # 3行3列, 从0,0开始, 行跨度, 列跨度
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax = plt.gca()  #get current axis
ax.spines['right'].set_color('none')  # 无色: 右边和顶部边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 设置x坐标轴为下边框
ax.yaxis.set_ticks_position('left')  # 设置y坐标轴为左边框
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# pic_4
ax1 = plt.subplot2grid((3,3), (1,2), colspan=1, rowspan=2)  # 3行3列, 从0,0开始, 行跨度, 列跨度
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax = plt.gca()  #get current axis
ax.spines['right'].set_color('none')  # 无色: 右边和顶部边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 设置x坐标轴为下边框
ax.yaxis.set_ticks_position('left')  # 设置y坐标轴为左边框
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))


# pic_5
ax1 = plt.subplot2grid((3,3), (2,0), colspan=2, rowspan=1)  # 3行3列, 从0,0开始, 行跨度, 列跨度
ax1.plot(x, y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax = plt.gca()  #get current axis
ax.spines['right'].set_color('none')  # 无色: 右边和顶部边框
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')  # 设置x坐标轴为下边框
ax.yaxis.set_ticks_position('left')  # 设置y坐标轴为左边框
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

plt.tight_layout()
plt.show()