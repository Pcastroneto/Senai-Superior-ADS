'''
Uma biblioteca para modelagem de tópicos e processamento de linguagem natural. 
Ele permite que os usuários treinem modelos de tópicos em grandes conjuntos de dados de texto e realizem outras tarefas de processamento de linguagem natural,
como extração de palavras-chave e detecção de sinônimos.

'''

import gensim
from gensim.models import Word2Vec

# Frases para treinamento
sentences = [
    ["o", "rato", "roeu", "a", "roupa"],
    ["a", "casa", "caiu"],
    ["o", "cachorro", "latiu", "muito"],
    ["eu", "amo", "programar"]
]

# Criando modelo Word2Vec com as frases
model = Word2Vec(sentences, min_count=1)

# Buscando palavras similares
similar_words = model.wv.most_similar('cachorro')

# Imprimindo resultados
print(similar_words)
