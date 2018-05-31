import numpy as np
import tensorflow as tf
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import re
from random import randint

numDimensions_embedding = 300
maxSeqLength_inputSize = 250
batchSize = 24
lstmUnits = 64
numClasses = 2
iterations = 100000

# https://github.com/adeshpande3/LSTM-Sentiment-Analysis/blob/master/Oriole%20LSTM.ipynb
wordsList = np.load('wordsList.npy')
print('Loaded the word list!')
wordsList = wordsList.tolist()  # Originally loaded as numpy array
wordsList = [word.decode('UTF-8') for word in wordsList]  # Encode words as UTF-8
wordVectors = np.load('wordVectors.npy')
print ('Loaded the word vectors!')

ids = np.load('idsMatrix.npy')


def getTrainBatch():
    labels = []
    arr = np.zeros([batchSize, maxSeqLength_inputSize])
    for i in range(batchSize):
        if (i % 2 == 0):
            num = randint(1,11499)
            labels.append([1,0])
        else:
            num = randint(13499,24999)
            labels.append([0,1])
        arr[i] = ids[num-1:num]
    return arr, labels

def getTestBatch():
    labels = []
    arr = np.zeros([batchSize, maxSeqLength_inputSize])
    for i in range(batchSize):
        num = randint(11499,13499)
        if (num <= 12499):
            labels.append([1,0])
        else:
            labels.append([0,1])
        arr[i] = ids[num-1:num]
    return arr, labels



tf.reset_default_graph()
labels = tf.placeholder(tf.float32, [batchSize, numClasses])
input_data = tf.placeholder(tf.int32, [batchSize, maxSeqLength_inputSize])
data = tf.Variable(tf.zeros([batchSize, maxSeqLength_inputSize, numDimensions_embedding]), dtype=tf.float32)
data = tf.nn.embedding_lookup(wordVectors, input_data)  # shape是 seq * embedding * batch 可以想象

lstmCell = tf.contrib.rnn.BasicLSTMCell(lstmUnits)
lstmCell = tf.contrib.rnn.DropoutWrapper(cell=lstmCell, output_keep_prob=0.75)
outputs, last_states = tf.nn.dynamic_rnn(lstmCell, data, dtype=tf.float32)

weight = tf.Variable(tf.truncated_normal([lstmUnits, numClasses]))
bias = tf.Variable(tf.constant(0.1, shape=[numClasses]))
outputs = tf.transpose(outputs, [1, 0, 2])
last = tf.gather(outputs, int(outputs.get_shape()[0]) - 1)
prediction = (tf.matmul(last, weight) + bias)


correctPred = tf.equal(tf.argmax(prediction,1), tf.argmax(labels,1))
accuracy = tf.reduce_mean(tf.cast(correctPred, tf.float32))

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=labels))
optimizer = tf.train.AdamOptimizer().minimize(loss)