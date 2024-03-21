'''
TensorFlow é uma biblioteca (open source também) para computação numérica que torna o aprendizado de máquina mais rápido e fácil com APIs que ajudam a utilizar as tecnologias do mesmo.
Aqui em exemplo de código tirado da internet:


import tensorflow as tf
from tensorflow import keras
import numpy as np

# Carregando o conjunto de dados de imagens de roupas
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalizando as imagens
train_images = train_images / 255.0
test_images = test_images / 255.0

# Definindo as classes de saída
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Definindo o modelo da rede neural
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

# Compilando o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinando o modelo
model.fit(train_images, train_labels, epochs=10)

# Avaliando o modelo
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nAcurácia do Teste:', test_acc)

# Fazendo previsões com o modelo
predictions = model.predict(test_images)



Neste exemplo, o TensorFlow é usado para construir um modelo de rede neural com uma camada de entrada, uma camada oculta e uma camada de saída.
O modelo é treinado com o conjunto de dados de imagens de roupas fashion_mnist e, em seguida, é usado para fazer previsões sobre novas imagens.

'''