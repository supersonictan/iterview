# -*- coding: utf-8 -*-
import tensorflow as tf
import os
import functools
import numpy as np
import models
import dataset

HIDDEN_SIZE = 128
NUM_LAYERS = 2
BATCH_SIZE = 64
# rnn层dropout保留率
RNN_KEEP_PROB = 0.5
# emb层dropout保留率
EMB_KEEP_PROB = 0.5


#tf.flags.DEFINE_string('buckets', '', 'buckets')
#FLAGS = tf.app.flags.FLAGS


# 数据
x = tf.placeholder(tf.int32, [None, None])
# 标签
y = tf.placeholder(tf.float32, [None, 1])
# emb层的dropout保留率
emb_keep = tf.placeholder(tf.float32)
# rnn层的dropout保留率
rnn_keep = tf.placeholder(tf.float32)

# 创建一个模型
model = models.Model(x, y, emb_keep, rnn_keep)

# 创建数据集对象
data = dataset.Dataset()

saver = tf.train.Saver()


with tf.Session() as sess:
    # 全局初始化
    sess.run(tf.global_variables_initializer())
    # 迭代训练
    for step in range(20000):
        # 获取一个batch进行训练
        x, y = data.next_batch(BATCH_SIZE)
        loss, _ = sess.run([model.loss, model.optimize],
                           {model.data: x, model.label: y, model.emb_keep: EMB_KEEP_PROB, model.rnn_keep: RNN_KEEP_PROB})
        # 输出loss
        if step % 100 == 0:
            print 'step {},loss is {}'.format(step, loss)
        # 保存模型
        if step % 1000 == 0:
             pass
            #print(os.path.join(FLAGS.buckets, 'model'))
            #saver.save(sess, os.path.join(FLAGS.buckets, 'model'), model.global_step)
            # saver.save(sess, os.path.join(settings.CKPT_PATH, settings.MODEL_NAME), model.global_step)