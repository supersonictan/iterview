# -*- coding: utf-8 -*-
import numpy as np

data = [i for i in range(0, 8)]
data2 = np.array(data)
print(data2)

print np.reshape(data2, (-1, 2, 1))

vocab = ('a', 'b', 'c')
int_to_vocab = dict(enumerate(vocab))
print(int_to_vocab)

drop = 'drop'
test = [drop for _ in range(3)]
print(test)