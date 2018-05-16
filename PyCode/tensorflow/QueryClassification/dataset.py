# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
import os

tf.flags.DEFINE_string('buckets', '', 'buckets')
FLAGS = tf.app.flags.FLAGS

class Dataset(object):
    def __init__(self, data_kind=0):
        """
        生成一个数据集对象
        :param data_kind: 决定了使用哪种数据集 0-训练集 1-开发集 2-测试集
        """
        self.data, self.labels = self.read_data()
        self.start = 0  # 记录当前batch位置
        self.data_size = len(self.data)  # 样例数

    def read_data(self):
        """
        从文件中加载数据
        :param data_kind:数据集种类 0-训练集 1-开发集 2-测试集
        :return:
        """
        # 获取数据集路径
        # data_path = [settings.TRAIN_DATA, settings.DEV_DATA, settings.TEST_DATA][data_kind]
        data = np.load('train_data.npy')
        labels = np.load('train_labels.npy')

        # data_path_fe = os.path.join(FLAGS.buckets, 'train_data.npy')
        # data_path_label = os.path.join(FLAGS.buckets, 'train_labels.npy')
        # print(data_path_fe)
        # data = np.load(data_path_fe)
        # labels = np.load(data_path_label)

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




if __name__ == '__main__':
    Dataset()