# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

num_epochs = 200  # 训练循环次数
batch_size = 128  # batch大小
rnn_size = 256  # lstm层中包含的unit个数
embed_dim = 300  # embedding layer的大小
seq_length = 32  # 训练步长
learning_rate = 0.01  # 学习率
show_every_n_batches = 8  # 每多少步打印一次训练信息
save_dir = './save'  # 保存session状态的位置


def create_lookup_tables(input_data):
    vocab = set(input_data)
    vocab_to_int = {word: idx for idx, word in enumerate(vocab)}  # 文字到数字的映射
    int_to_vocab = dict(enumerate(vocab))  # 数字到文字的映射
    return vocab_to_int, int_to_vocab


def get_inputs():
    inputs = tf.placeholder(tf.int32, [None, None], name='inputs')
    targets = tf.placeholder(tf.int32, [None, None], name='targets')
    learning_rate = tf.placeholder(tf.float32, name='learning_rate')

    return inputs, targets, learning_rate


# 创建rnn cell，使用lstm cell，并创建相应层数的lstm层，应用dropout，以及初始化lstm层状态。
def get_init_cell():
    num_layers = 3  # lstm层数
    cell = tf.contrib.rnn.BasicLSTMCell(256)  # 256维的lstm cell
    drop = tf.contrib.rnn.DropoutWrapper(cell, output_keep_prob=0.8)  # 使用dropout机制防止overfitting等
    cell = tf.contrib.rnn.MultiRNNCell([drop for _ in range(2)])  # 创建2层lstm层
    init_state = cell.zero_state(128, tf.float32)  # 初始化状态为0.0
    # 使用tf.identify给init_state取个名字，后面生成文字的时候，要使用这个名字来找到缓存的state
    init_state = tf.identity(init_state, name='init_state')

    return cell, init_state


def get_embed(input_data, vocab_size, embed_dim):
    # word * 256 矩阵
    embedding = tf.Variable(tf.random_uniform((vocab_size, embed_dim)), dtype=tf.float32)
    # 让tensorflow帮我们创建lookup table
    return tf.nn.embedding_lookup(embedding, input_data)


def build_rnn(cell, inputs):
    outputs, final_state = tf.nn.dynamic_rnn(cell, inputs, dtype=tf.float32)
    # 同样给final_state一个名字，后面要重新获取缓存
    final_state = tf.identity(final_state, name="final_state")

    return outputs, final_state


# 用上面定义的方法创建rnn网络，并接入最后一层fully_connected layer计算rnn的logits
def build_nn(cell, rnn_size, input_data, vocab_size, embed_dim):

    # 创建embedding layer
    embed = get_embed(input_data, vocab_size, rnn_size)

    # 计算outputs 和 final_state
    outputs, final_state = build_rnn(cell, embed)

    # remember to initialize weights and biases, or the loss will stuck at a very high point
    logits = tf.contrib.layers.fully_connected(outputs, vocab_size, activation_fn=None,
                                               weights_initializer = tf.truncated_normal_initializer(stddev=0.1),
                                               biases_initializer=tf.zeros_initializer())

    return logits, final_state


def get_batches(int_text, batch_size, seq_length):
    characters_per_batch = batch_size * seq_length
    num_batches = len(int_text) // characters_per_batch

    # clip arrays to ensure we have complete batches for inputs, targets same but moved one unit over
    input_data = np.array(int_text[: num_batches * characters_per_batch])
    target_data = np.array(int_text[1: num_batches * characters_per_batch + 1])

    inputs = input_data.reshape(batch_size, -1)
    targets = target_data.reshape(batch_size, -1)

    inputs = np.split(inputs, num_batches, 1)
    targets = np.split(targets, num_batches, 1)

    batches = np.array(list(zip(inputs, targets)))
    batches[-1][-1][-1][-1] = batches[0][0][0][0]

    return batches