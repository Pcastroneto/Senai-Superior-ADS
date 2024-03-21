'''
Uma biblioteca Python para processamento de linguagem natural. 
Ele oferece uma variedade de ferramentas para tarefas como classificação de texto, análise de sentimentos e correção ortográfica.
'''

from textblob import TextBlob

frase = "Eu amo programar"
tb = TextBlob(frase)

polaridade = tb.sentiment.polarity
subjetividade = tb.sentiment.subjectivity

print("Frase: ", frase)
print("Polaridade: ", polaridade)
print("Subjetividade: ", subjetividade)
