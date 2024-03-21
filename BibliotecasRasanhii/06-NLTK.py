'''
Essa biblioteca é voltada para contexto acadêmico. 
Ela contém vários algoritmos já implementados para resolver os mais diversos tipos de tratamento.
'''

import nltk

# defina a frase a ser tokenizada
frase = "O gato está sobre o tapete."

# tokenização da frase em palavras
palavras = nltk.word_tokenize(frase)

# exibir as palavras
print(palavras)
