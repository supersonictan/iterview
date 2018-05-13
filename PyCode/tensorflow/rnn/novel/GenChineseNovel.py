# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.contrib import rnn
import numpy as np
import helper
#from tensorflow.contrib import seq2seq



dir = './data/寒门首辅'
text = helper.load_text(dir)
text = text[:1000]
vocab_to_int = {}
int_to_vocab = {}




num_epochs = 200  # 训练循环次数
batch_size = 128  # batch大小
rnn_size = 256  # lstm层中包含的unit个数
embed_dim = 300  # embedding layer的大小
seq_length = 32  # 训练步长
learning_rate = 0.01  # 学习率
show_every_n_batches = 8  # 每多少步打印一次训练信息
save_dir = './save'  # 保存session状态的位置




# 定义 lookup table
def create_lookup_tables(input_data):
    global vocab_to_int
    global int_to_vocab
    vocab = set(input_data)
    vocab_to_int = {word: idx for idx, word in enumerate(vocab)}  # 文字到数字的映射
    int_to_vocab = dict(enumerate(vocab))  # 数字到文字的映射


def get_inputs():
    inputs = tf.placeholder(tf.int32, [None, None], name='inputs')
    targets = tf.placeholder(tf.int32, [None, None], name='targets')
    return inputs, targets


# 创建rnn cell，使用lstm cell，并创建相应层数的 lstm 层，应用 dropout，以及初始化 lstm 层状态。
def get_init_cell():
    cell = rnn.BasicLSTMCell(256)  # hidden_unit:256维的lstm cell
    drop = rnn.DropoutWrapper(cell, output_keep_prob=0.8)  # 使用dropout机制防止overfitting等
    cell = rnn.MultiRNNCell([drop for _ in range(2)])  # 创建2层lstm层
    init_state = cell.zero_state(128, tf.float32)  # 初始化状态为0.0
    # 使用tf.identify给init_state取个名字，后面生成文字的时候，要使用这个名字来找到缓存的state
    init_state = tf.identity(init_state, name='init_state')

    return cell, init_state



if __name__ == '__main__':
    create_lookup_tables(text)
    print(vocab_to_int)
    print(int_to_vocab)




"""
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
    # 创建 embedding layer
    embed = get_embed(input_data, vocab_size, rnn_size)
    # 计算outputs 和 final_state
    outputs, final_state = build_rnn(cell, embed)
    # remember to initialize weights and biases, or the loss will stuck at a very high point
    logits = tf.contrib.layers.fully_connected(outputs, vocab_size, activation_fn=None,
                                               weights_initializer = tf.truncated_normal_initializer(stddev=0.1),
                                               biases_initializer=tf.zeros_initializer())

    return logits, final_state


# 计算有多少个batch可以创建
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


train_graph = tf.Graph()
with train_graph.as_default():
    # 文字总量
    vocab_size = len(int_to_vocab)

    # 获取模型的输入，目标以及学习率节点，这些都是tf的placeholder
    input_text, targets, lr = get_inputs()

    # 输入数据的shape
    input_data_shape = tf.shape(input_text)

    # 创建rnn的cell和初始状态节点，rnn的cell已经包含了lstm，dropout
    # 这里的rnn_size表示每个lstm cell中包含了多少的神经元
    cell, initial_state = get_init_cell(input_data_shape[0], rnn_size)

    # 创建计算loss和finalstate的节点
    logits, final_state = build_nn(cell, rnn_size, input_text, vocab_size, embed_dim)

    # 使用softmax计算最后的预测概率
    probs = tf.nn.softmax(logits, name='probs')

    # 计算loss
    cost = seq2seq.sequence_loss(
        logits,
        targets,
        tf.ones([input_data_shape[0], input_data_shape[1]]))

    # 使用Adam提督下降
    optimizer = tf.train.AdamOptimizer(lr)

    # 裁剪一下Gradient输出，最后的gradient都在[-1, 1]的范围内
    gradients = optimizer.compute_gradients(cost)
    capped_gradients = [(tf.clip_by_value(grad, -1., 1.), var) for grad, var in gradients if grad is not None]
    train_op = optimizer.apply_gradients(capped_gradients)


# 开始训练模型
# 获得训练用的所有batch
batches = get_batches(int_text, batch_size, seq_length)

# 打开session开始训练，将上面创建的graph对象传递给session
with tf.Session(graph=train_graph) as sess:
    sess.run(tf.global_variables_initializer())

    for epoch_i in range(num_epochs):
        state = sess.run(initial_state, {input_text: batches[0][0]})

        for batch_i, (x, y) in enumerate(batches):
            feed = {
                input_text: x,
                targets: y,
                initial_state: state,
                lr: learning_rate}
            train_loss, state, _ = sess.run([cost, final_state, train_op], feed)

            # 打印训练信息
            if (epoch_i * len(batches) + batch_i) % show_every_n_batches == 0:
                print('Epoch {:>3} Batch {:>4}/{}   train_loss = {:.3f}'.format(
                    epoch_i,
                    batch_i,
                    len(batches),
                    train_loss))

    # 保存模型
    saver = tf.train.Saver()
    saver.save(sess, save_dir)
    print('Model Trained and Saved')


# 将使用到的变量保存起来，以便下次直接读取。
helper.save_params((seq_length, save_dir))


# 要使用保存的模型，我们要讲保存下来的变量（tensor）通过指定的name获取到
def get_tensors(loaded_graph):
    inputs = loaded_graph.get_tensor_by_name("inputs:0")

    initial_state = loaded_graph.get_tensor_by_name("init_state:0")

    final_state = loaded_graph.get_tensor_by_name("final_state:0")

    probs = loaded_graph.get_tensor_by_name("probs:0")

    return inputs, initial_state, final_state, probs


def pick_word(probabilities, int_to_vocab):
    num_word = np.random.choice(len(int_to_vocab), p=probabilities)

    return int_to_vocab[num_word]


# 使用训练好的模型来生成自己的小说
# 生成文本的长度
gen_length = 500

# 文章开头的字，指定一个即可，这个字必须是在训练词汇列表中的
prime_word = '我'

loaded_graph = tf.Graph()
with tf.Session(graph=loaded_graph) as sess:
    # 加载保存过的session
    loader = tf.train.import_meta_graph(load_dir + '.meta')
    loader.restore(sess, load_dir)

    # 通过名称获取缓存的tensor
    input_text, initial_state, final_state, probs = get_tensors(loaded_graph)

    # 准备开始生成文本
    gen_sentences = [prime_word]
    prev_state = sess.run(initial_state, {input_text: np.array([[1]])})

    # 开始生成文本
    for n in range(gen_length):
        dyn_input = [[vocab_to_int[word] for word in gen_sentences[-seq_length:]]]
        dyn_seq_length = len(dyn_input[0])

        probabilities, prev_state = sess.run(
            [probs, final_state],
            {input_text: dyn_input, initial_state: prev_state})

        pred_word = pick_word(probabilities[dyn_seq_length - 1], int_to_vocab)

        gen_sentences.append(pred_word)

    # 将标点符号还原
    novel = ''.join(gen_sentences)
    for key, token in token_dict.items():
        ending = ' ' if key in ['\n', '（', '“'] else ''
        novel = novel.replace(token.lower(), key)
    # novel = novel.replace('\n ', '\n')
    # novel = novel.replace('（ ', '（')

    print(novel)

"""
