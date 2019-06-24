import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


"""
变量加减
"""
x = tf.Variable([1,2])
a = tf.Variable([3,3])
# 减法op
sub = tf.subtract(x, a)
# 加法op
add = tf.add(x, sub)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))