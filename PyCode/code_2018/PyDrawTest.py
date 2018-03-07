# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from scipy.stats import normaltest
from sklearn import metrics

## ----------------------------------线图-------------------------
x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='Line1')  #Line1 是线条名称
plt.plot(x2, y2, label='Line2')

# x,y轴的名字, 图片title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Title')

# 生成图例
plt.legend()
plt.show()


## ----------------------------------线图-------------------------
bar_x = [1,3,5,7,9]
bar_y = [5,2,7,8,2]
bar_x2 = [2,4,6,8,10]
bar_y2 = [8,6,2,5,6]
plt.bar(bar_x, bar_y, color='r')
plt.bar(bar_x2, bar_y2, color='g')
plt.show()