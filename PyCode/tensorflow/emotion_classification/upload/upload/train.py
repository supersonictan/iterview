# -*- coding: utf-8 -*-
import tensorflow as tf
import dataset
import os
import functools
import numpy as np

HIDDEN_SIZE = 128
NUM_LAYERS = 2

# 源数据路径
ORIGIN_NEG = 'data/rt-polarity.neg'
ORIGIN_POS = 'data/rt-polarity.pos'

# 转码后的数据路径
NEG_TXT = 'data/neg.txt'
POS_TXT = 'data/pos.txt'

# 词汇表路径
VOCAB_PATH = 'data/vocab.txt'

# 词向量路径
NEG_VEC = 'data/neg.vec'

POS_VEC = 'data/pos.vec'
# 训练集路径
TRAIN_DATA = 'data/train'
# 开发集路径
DEV_DATA = 'data/dev'
# 测试集路径
TEST_DATA = 'data/test'
# 模型保存路径
CKPT_PATH = 'ckpt'
# 模型名称
MODEL_NAME = 'model'
# 词汇表大小
VOCAB_SIZE = 10000
# 初始学习率
LEARN_RATE = 0.0001
# 学习率衰减
LR_DECAY = 0.99
# 衰减频率
LR_DECAY_STEP = 1000
# 总训练次数
TRAIN_TIMES = 2000
# 显示训练loss的频率
SHOW_STEP = 10
# 保存训练模型的频率
SAVE_STEP = 100
# 训练集占比
TRAIN_RATE = 0.8
# 开发集占比
DEV_RATE = 0.1
# 测试集占比
TEST_RATE = 0.1
# BATCH大小
BATCH_SIZE = 64
# emb层dropout保留率
EMB_KEEP_PROB = 0.5
# rnn层dropout保留率
RNN_KEEP_PROB = 0.5
# 移动平均衰减率
EMA_RATE = 0.99

tf.flags.DEFINE_string('buckets', '', 'buckets')
FLAGS = tf.app.flags.FLAGS




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
        embedding = tf.get_variable('embedding', [VOCAB_SIZE, HIDDEN_SIZE])
        # 使用dropout的LSTM
        lstm_cell = [tf.nn.rnn_cell.DropoutWrapper(tf.nn.rnn_cell.BasicLSTMCell(HIDDEN_SIZE), self.rnn_keep) for _ in
                     range(NUM_LAYERS)]
        # 构建循环神经网络
        cell = tf.nn.rnn_cell.MultiRNNCell(lstm_cell)
        # 生成词嵌入矩阵，并进行dropout
        input = tf.nn.embedding_lookup(embedding, self.data)
        dropout_input = tf.nn.dropout(input, self.emb_keep)
        # 计算rnn的输出
        outputs, last_state = tf.nn.dynamic_rnn(cell, dropout_input, dtype=tf.float32)
        # 做二分类问题，这里只需要最后一个节点的输出
        last_output = outputs[:, -1, :]
        # 求最后节点输出的线性加权和
        weights = tf.Variable(tf.truncated_normal([HIDDEN_SIZE, 1]), dtype=tf.float32, name='weights')
        bias = tf.Variable(0, dtype=tf.float32, name='bias')

        logits = tf.matmul(last_output, weights) + bias

        return logits

    @define_scope
    def ema(self):
        """
        定义移动平均
        :return:
        """
        ema = tf.train.ExponentialMovingAverage(EMA_RATE, self.global_step)
        return ema

    @define_scope
    def loss(self):
        """
        定义损失函数，这里使用交叉熵
        :return:
        """
        loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=self.label, logits=self.predict)
        loss = tf.reduce_mean(loss)
        return loss

    @define_scope
    def global_step(self):
        """
        step,没什么好说的，注意指定trainable=False
        :return:
        """
        global_step = tf.Variable(0, trainable=False)
        return global_step

    @define_scope
    def optimize(self):
        """
        定义反向传播过程
        :return:
        """
        # 学习率衰减
        learn_rate = tf.train.exponential_decay(LEARN_RATE, self.global_step, LR_DECAY_STEP,
                                                LR_DECAY)
        # 反向传播优化器
        optimizer = tf.train.AdamOptimizer(learn_rate).minimize(self.loss, global_step=self.global_step)
        # 移动平均操作
        ave_op = self.ema.apply(tf.trainable_variables())
        # 组合构成训练op
        with tf.control_dependencies([optimizer, ave_op]):
            train_op = tf.no_op('train')
        return train_op

    @define_scope
    def acc(self):
        """
        定义模型acc计算过程
        :return:
        """
        # 对前向传播的结果求sigmoid
        output = tf.nn.sigmoid(self.predict)
        # 真负类
        ok0 = tf.logical_and(tf.less_equal(output, 0.5), tf.equal(self.label, 0))
        # 真正类
        ok1 = tf.logical_and(tf.greater(output, 0.5), tf.equal(self.label, 1))
        # 一个数组，所有预测正确的都为True,否则False
        ok = tf.logical_or(ok0, ok1)
        # 先转化成浮点型，再通过求平均来计算acc
        acc = tf.reduce_mean(tf.cast(ok, dtype=tf.float32))
        return acc


BATCH_SIZE = BATCH_SIZE

# 数据
x = tf.placeholder(tf.int32, [None, None])
# 标签
y = tf.placeholder(tf.float32, [None, 1])
# emb层的dropout保留率
emb_keep = tf.placeholder(tf.float32)
# rnn层的dropout保留率
rnn_keep = tf.placeholder(tf.float32)

# 创建一个模型
model = Model(x, y, emb_keep, rnn_keep)

# 创建数据集对象
data = dataset.Dataset(0)

saver = tf.train.Saver()


class Dataset(object):
    def __init__(self, data_kind=0):
        """
        生成一个数据集对象
        :param data_kind: 决定了使用哪种数据集 0-训练集 1-开发集 2-测试集
        """
        self.data, self.labels = self.read_data(data_kind)
        self.start = 0  # 记录当前batch位置
        self.data_size = len(self.data)  # 样例数

    def read_data(self, data_kind):
        """
        从文件中加载数据
        :param data_kind:数据集种类 0-训练集 1-开发集 2-测试集
        :return:
        """
        # 获取数据集路径
        # data_path = [settings.TRAIN_DATA, settings.DEV_DATA, settings.TEST_DATA][data_kind]
        # data = np.load(data_path + '_data.npy')
        # labels = np.load(data_path + '_labels.npy')

        data_path_fe = os.path.join(FLAGS.buckets, '/train_data.npy')
        data_path_label = os.path.join(FLAGS.buckets, '/train_labels.npy')
        data = np.load(data_path_fe)
        labels = np.load(data_path_label)

        # save_path = os.path.join(FLAGS.buckets, '/filname')
        # 加载

        return data, labels

    def next_batch(self, batch_size):
        """
        获取一个大小为batch_size的batch
        :param batch_size: batch大小
        :return:
        """
        start = self.start
        end = min(start + batch_size, self.data_size)
        self.start = end
        # 当遍历完成后回到起点
        if self.start >= self.data_size:
            self.start = 0
        # 返回一个batch的数据和标签
        return self.data[start:end], self.labels[start:end]

with tf.Session() as sess:
    # 全局初始化
    sess.run(tf.global_variables_initializer())
    # 迭代训练
    for step in range(TRAIN_TIMES):
        # 获取一个batch进行训练
        x, y = data.next_batch(BATCH_SIZE)
        loss, _ = sess.run([model.loss, model.optimize],
                           {model.data: x, model.label: y, model.emb_keep: EMB_KEEP_PROB,
                            model.rnn_keep: RNN_KEEP_PROB})
        # 输出loss
        if step % SHOW_STEP == 0:
            print 'step {},loss is {}'.format(step, loss)
        # 保存模型
        if step % SAVE_STEP == 0:
            saver.save(sess, os.path.join(FLAGS.buckets, '/model'), model.global_step)
            # saver.save(sess, os.path.join(settings.CKPT_PATH, settings.MODEL_NAME), model.global_step)