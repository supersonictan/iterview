#!/usr/bin/python
# -*- coding=utf-8-*-
import tensorflow as tf
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 创建1*2矩阵，2*1矩阵
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[3.], [3.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
    result = sess.run([product])
    print result
