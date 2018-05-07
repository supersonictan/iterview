# -*- coding: utf-8 -*-
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#  set random seed for comparing the two result calculations
tf.set_random_seed(1)

# this is data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

training_iters = 100000
batch_size = 128

n_inputs = 28  # MNIST data input (img shape: 28*28)
n_steps = 28   # time steps
n_hidden_units = 128  # neurons in hidden layer
n_classes = 10  # MNIST classes (0-9 digits)

# tf Graph input
x = tf.placeholder(tf.float32, [None, n_steps, n_inputs])
y = tf.placeholder(tf.float32, [None, n_classes])

# Define weights
weights = {
    # (28, 128)
    'in': tf.Variable(tf.random_normal([n_inputs, n_hidden_units])),
    # (128, 10)
    'out': tf.Variable(tf.random_normal([n_hidden_units, n_classes]))
}
biases = {
    # (128, )
    'in': tf.Variable(tf.constant(0.1, shape=[n_hidden_units, ])),
    # (10, )
    'out': tf.Variable(tf.constant(0.1, shape=[n_classes, ]))
}


def RNN(X, weights, biases):
    # hidden layer for input to cell
    ########################################
    X = tf.reshape(X, [-1, n_inputs])  # X输入值:128,28,28,需要变为:128*28,28. -1表示128,28总起来

    # X_in = (128 batch * 28 steps, 128 hidden)
    X_in = tf.matmul(X, weights['in']) + biases['in']  # 结果128*28 * 128
    X_in = tf.reshape(X_in, [-1, n_steps, n_hidden_units])  # 变为128 * 28 * 128

    # cell
    ##########################################
    cell = tf.contrib.rnn.BasicLSTMCell(n_hidden_units)  # lstm cell is divided into two parts (c_state, h_state)
    init_state = cell.zero_state(batch_size, dtype=tf.float32)  # 全零state自己学习记忆

    # output 是个tensor
    outputs, final_state = tf.nn.dynamic_rnn(cell, X_in, initial_state=init_state, time_major=False)  # 时间维度在 steps 第二个维度上

    # hidden layer for output as the final results
    #############################################
    #  unpack to list[(batch,output)...] * nstep
    outputs = tf.unstack(tf.transpose(outputs, [1, 0, 2]))  # unpack把主维度变为list中多少个元素
    results = tf.matmul(outputs[-1], weights['out']) + biases['out']  # outputs[-1]表示最后一个输出

    return results


pred = RNN(x, weights, biases)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=y))
train_op = tf.train.AdamOptimizer(0.001).minimize(cost)

correct_pred = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    step = 0
    while step * batch_size < training_iters:
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape([batch_size, n_steps, n_inputs])
        sess.run([train_op], feed_dict={
            x: batch_xs,
            y: batch_ys,
        })
        if step % 20 == 0:
            print(sess.run(accuracy, feed_dict={
            x: batch_xs,
            y: batch_ys,
            }))
        step += 1