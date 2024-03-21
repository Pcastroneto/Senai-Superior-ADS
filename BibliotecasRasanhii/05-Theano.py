'''
É uma biblioteca usada para manipular e avaliar expressões matemáticas, especialmente aquelas com valor de matriz.
No Theano, os cálculos são expressos usando uma sintaxe do tipo NumPy e compilados para serem executados com eficiência nas arquiteturas de CPU ou GPU.
Um exemplo é:


import theano
import theano.tensor as T
import numpy as np

x = T.matrix('x')
y = T.vector('y')

w1 = theano.shared(np.random.randn(2, 2), name='w1')
w2 = theano.shared(np.random.randn(2), name='w2')

a1 = T.nnet.sigmoid(T.dot(x, w1))
y_hat = T.nnet.sigmoid(T.dot(a1, w2))

cost = T.mean((y - y_hat)**2)

learning_rate = 0.1
updates = [
    (w1, w1 - learning_rate * T.grad(cost, w1)),
    (w2, w2 - learning_rate * T.grad(cost, w2))
]


learning_rate = 0.1
updates = [
    (w1, w1 - learning_rate * T.grad(cost, w1)),
    (w2, w2 - learning_rate * T.grad(cost, w2))
]


Neste exemplo, estamos treinando a rede neural para aprender a função XOR e, em seguida, testando a saída prevista pela rede.
'''