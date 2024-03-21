'''
Esta biblioteca pode ser usada para substituir palavras-chave em frases ou extrair palavras-chave de frases.
'''

# Importando a biblioteca flashtext
from flashtext import KeywordProcessor

# Criando uma instância da classe KeywordProcessor
palavra = KeywordProcessor()

# Adicionando sinônimos à biblioteca
palavra.add_keyword('carro', 'automóvel')
palavra.add_keyword('casa', 'humilde residência')

# Texto de entrada
texto = 'Eu quero comprar um carro e uma casa.'

# Substituindo palavras-chave usando a biblioteca
texto_modificado = palavra.replace_keywords(texto)

# Imprimindo o texto modificado
print(texto_modificado)
