'''
Keras é uma biblioteca open source criada para Deep Learning com Python. 
Ela é utilizado na criação de redes neurais para resolução de várias tarefas diferentes, como classificação de imagens, detecção de objetos e regressão.
O TesorFlow é uma biblioteca muito grande e vasta, então não vou instala-la aqui, porém um exemplo de código que pesquisei é:



import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Define o modelo da rede neural
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(784,)),
    layers.Dense(10, activation='softmax')
])

# Compila o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Carrega os dados de treinamento
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Pré-processa os dados de treinamento
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

# Treina o modelo
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Avalia o modelo
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Test accuracy:', test_acc)



Neste exemplo, estamos treinando uma rede neural para reconhecer dígitos escritos à mão usando o conjunto de dados MNIST. 
O modelo é composto por duas camadas densas e é treinado usando o otimizador Adam e a função de perda cross-entropy categórica. 
Depois de treinado, o modelo é avaliado no conjunto de teste e a acurácia é exibida na saída. De acordo com pesquisas.
'''