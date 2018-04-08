#!/usr/bin/python
# -*- coding=utf-8-*-
import tensorflow as tf
import re
import numpy as np
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

# 创建1*2矩阵，2*1矩阵
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[3.], [3.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
    result = sess.run([product])
    print result


if __name__ == '__main__':
    s1 = "人生剧场：青春篇 爱欲篇 残侠篇sss"
    s1 = re.sub(r'！|!|·|,|▪', "", s1)
    s1 = re.search(".*(篇)$", s1)
    if s1 is not None:
        print("true")
    print(s1)