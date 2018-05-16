# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import collections
import numpy as np
import models


VOCAB_PATH = 'data/vocab.txt'
NEG_TXT = 'data/neg.txt'
POS_TXT = 'data/pos.txt'
NEG_VEC = 'data/neg.vec'
POS_VEC = 'data/pos.vec'
TRAIN_DATA = 'train_data'
TRAIN_LABEL = 'train_labels'


def create_vocab():
    """
    创建词汇表，写入文件中
    :return:
    """
    # 存放出现的所有单词
    word_list = []
    # 从文件中读取数据，拆分单词
    with open(NEG_TXT, 'r') as f:
        f_lines = f.readlines()
        for line in f_lines:
            words = line.strip().split('@')
            word_list.extend(words)

    with open(POS_TXT, 'r') as f:
        f_lines = f.readlines()
        for line in f_lines:
            words = line.strip().split('@')
            word_list.extend(words)

    # 统计单词出现的次数
    counter = collections.Counter(word_list)

    sorted_words = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    # 选取高频词
    word_list = [word[0] for word in sorted_words]

    word_list = ['<unkown>'] + word_list[:models.VOCAB_SIZE-1]
    # 将词汇表写入文件中
    with open(VOCAB_PATH, 'w') as f:
        for word in word_list:
            f.write(word + '\n')


def create_vec(txt_path, vec_path):
    """
    根据词汇表生成词向量
    :param txt_path: 影评文件路径
    :param vec_path: 输出词向量路径
    :return:
    """
    # 获取单词到编号的映射
    word2id = read_word_to_id_dict()
    # 将语句转化成向量
    vec = []  # [[], [], []]
    with open(txt_path, 'r') as f:
        f_lines = f.readlines()
        for line in f_lines:
            tmp_vec = [str(get_id_by_word(word, word2id)) for word in line.strip().split('@')]
            vec.append(tmp_vec)
    # 写入文件中
    with open(vec_path, 'w') as f:
        for tmp_vec in vec:
            f.write(' '.join(tmp_vec) + '\n')


def shuffle_all_data():
    """
    填充数据，生成np数组
    打乱数据，写入文件中
    :return:
    """
    all_data = []
    all_labels = []
    # 添加正样本
    with open(POS_VEC, 'r') as f:
        f_lines = f.readlines()
        for line in f_lines:
            tmp_data = [int(word) for word in line.strip().split()]
            tmp_label = [1, ]
            all_data.append(tmp_data)
            all_labels.append(tmp_label)

    # 添加负样本
    with open(NEG_VEC, 'r') as f:
        f_lines = f.readlines()
        for line in f_lines:
            tmp_data = [int(word) for word in line.strip().split()]
            tmp_label = [0, ]
            all_data.append(tmp_data)
            all_labels.append(tmp_label)

    # 计算影评的最大长度
    maxlen = max(map(len, all_data))
    # 填充数据
    padding_data = np.zeros([len(all_data), maxlen], dtype=np.int32)
    for row in range(len(all_data)):
        padding_data[row, :len(all_data[row])] = all_data[row]
    label = np.array(all_labels)
    # 打乱数据
    state = np.random.get_state()
    np.random.shuffle(padding_data)
    np.random.set_state(state)
    np.random.shuffle(label)
    # 保存数据
    np.save(TRAIN_DATA, padding_data)
    np.save(TRAIN_LABEL, label)


def read_vocab_list():
    """
    读取词汇表
    :return:由词汇表中所有单词组成的列表
    """
    with open(VOCAB_PATH, 'r') as f:
        vocab_list = f.read().strip().split('\n')
    return vocab_list
def read_word_to_id_dict():
    """
    生成一个单词到编号的映射
    :return:单词到编号的字典
    """
    vocab_list = read_vocab_list()
    word2id = dict(zip(vocab_list, range(len(vocab_list))))
    return word2id
def get_id_by_word(word, word2id):
    """
    给定一个单词和字典，获得单词在字典中的编号
    :param word: 给定单词
    :param word2id: 单词到编号的映射
    :return: 若单词在字典中，返回对应的编号 否则，返回word2id['<unkown>']
    """
    if word in word2id:
        return word2id[word]
    else:
        return word2id['<unkown>']


if __name__ == '__main__':
    create_vocab()
    create_vec(NEG_TXT, NEG_VEC)
    create_vec(POS_TXT, POS_VEC)
    shuffle_all_data()
