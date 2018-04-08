#!/usr/bin/python
# -*- coding=utf-8-*-
import tensorflow as tf
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3
print(x_data)

# 结构
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  #1维,范围[-1,1]
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
# end 结构

sess = tf.Session()  # 会话控制语句
sess.run(init)

for step in range(150):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

