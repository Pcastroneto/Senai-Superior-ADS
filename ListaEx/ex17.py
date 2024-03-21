print('Escreva uma lista de nomes\n')

lista = []
novalista = []
for i in range(10):
    lista.append(str(input('Escreva um nome: ').capitalize()))
for x in lista:
    if x[0] == 'E':
        novalista.append(x)
print("Os nomes com a letra 'E' são:", novalista)