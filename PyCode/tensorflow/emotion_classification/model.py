# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import functools
import settings

HIDDEN_SIZE = 128
NUM_LAYERS = 2


def doublewrap(function):
    @functools.wraps(function)
    def decorator(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            return function(args[0])
        else:
            return lambda wrapee: function(wrapee, *args, **kwargs)

    return decorator


@doublewrap
def define_scope(function, scope=None, *args, **kwargs):
    attribute = '_cache_' + function.__name__
    name = scope or function.__name__

    @property
    @functools.wraps(function)
    def decorator(self):
        if not hasattr(self, attribute):
            with tf.variable_scope(name, *args, **kwargs):
                setattr(self, attribute, function(self))
        return getattr(self, attribute)

    return decorator


class Model(object):
    def __init__(self, data, lables, emb_keep, rnn_keep):
        """
        神经网络模型
        :param data:数据
        :param lables: 标签
        :param emb_keep: emb层保留率
        :param rnn_keep: rnn层保留率
        """
        self.data = data
        self.label = lables
        self.emb_keep = emb_keep
        self.rnn_keep = rnn_keep
        self.predict
        self.loss
        self.global_step
        self.ema
        self.optimize
        self.acc


    @define_scope
    def predict(self):
        """
        定义前向传播过程
        :return:
        """
        # 词嵌入矩阵权重
        embedding = tf.get_variable('embedding', [settings.VOCAB_SIZE, HIDDEN_SIZE])
        # 定义 cell
        cell = tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE)
        # Dropout
        drop = tf.nn.rnn_cell.DropoutWrapper(cell, self.rnn_keep)
        # 使用dropout的LSTM
        lstm_cell = [drop for _ in range(NUM_LAYERS)]
        # 构建循环神经网络
        cell = tf.nn.rnn_cell.MultiRNNCell(lstm_cell)
        # 生成词嵌入矩阵，并进行dropout
        input = tf.nn.embedding_lookup(embedding, self.data)
        dropout_input = tf.nn.dropout(input, self.emb_keep)
        # 计算rnn的输出 output:[﻿batch_size, num_steps, size]
        outputs, last_state = tf.nn.dynamic_rnn(cell, dropout_input, dtype=tf.float32)
        # 做二分类问题，这里只需要最后一个节点的输出
        last_output = outputs[:, -1, :]
        # 求最后节点输出的线性加权和
        weights = tf.Variable(tf.truncated_normal([HIDDEN_SIZE, 1]), dtype=tf.float32, name='weights')
        bias = tf.Variable(0, dtype=tf.float32, name='bias')

        logits = tf.matmul(last_output, weights) + bias

        return logits


if __name__ == '__main__':
    print tf.__version__
    a = np.ones((3, 3))
    print(a)
    b = np.array([1, 2, 3])
    tf.matmul(a, b)
