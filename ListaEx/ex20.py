lista = []
novalista = []

print('Digite uma lista de palavras!!\n')
n = 0
for i in range(5):
    lista.append(str(input('Digite uma palavra: ')))

for x in lista:
    num = len(lista[n])
    if num%2 == 1:
        novalista.append(lista[n])
    n+=1

print('Essa é a lista com as palavras com o número impar de letras: ', novalista)