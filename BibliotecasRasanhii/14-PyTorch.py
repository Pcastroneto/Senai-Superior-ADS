'''
PyTorch é uma biblioteca de aprendizado de máquina de código aberto para Python que é amplamente utilizada para construir e treinar redes neurais. 
Ela fornece uma estrutura flexível para a construção de modelos de aprendizado profundo.
Como o exemplo:


import torch

# Definindo o tensor
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprimindo o tensor
print(x)

# Definindo uma matriz de pesos
w = torch.randn(3, 3)

# Multiplicando o tensor pela matriz de pesos
y = torch.matmul(x, w)

# Imprimindo o resultado
print(y)


Este código cria um tensor de 3x3, define uma matriz de pesos aleatórios de 3x3 e multiplica o tensor pela matriz de pesos. 
Por fim, ele imprime o resultado.
'''