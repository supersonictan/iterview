#!/usr/bin/python
# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def add_layer(inputs, in_size, out_size, af=None):
    with tf.name_scope('layer'):
        with tf.name_scope('weights'):
            W = tf.Variable(tf.random_normal([in_size, out_size]), name='W')
        with tf.name_scope('bias'):
            b = tf.Variable(tf.zeros([1, out_size]) + 0.1, name='bias')
        with tf.name_scope('Wx_plus_b'):
            wx_plus_b = tf.matmul(inputs, W) + b
        if af is None:
            outputs = wx_plus_b
        else:
            outputs = af(wx_plus_b)
        return outputs


# [-1,1] 300 lines
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
# mean:0 sd:0.05
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise

# 调用的入参
with tf.name_scope('inputs'):
    xs = tf.placeholder(tf.float32, [None, 1], name='x_input')
    ys = tf.placeholder(tf.float32, [None, 1], name='y_input')

# 隐层: 输入data只有一个特征, 一个节点
l1 = add_layer(xs, 1, 10, af=tf.nn.relu)
# 输出层
prediction = add_layer(l1, 10, 1, af=None)

with tf.name_scope('loss'):
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))

with tf.name_scope('train'):
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
writer = tf.summary.FileWriter("logs/", sess.graph)
sess.run(init)

# 绘制框图
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
#plt.ion()  # 非阻塞的画图python3.3以后
plt.show(block=False)  # 非阻塞的画图(old version)

for i in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        #print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))  # loss need compute
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        predict_val = sess.run(prediction, feed_dict={xs: x_data})
        lines = ax.plot(x_data, predict_val, 'r-', lw=5)
        plt.pause(1)
