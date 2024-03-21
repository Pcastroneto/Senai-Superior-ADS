lista = []

print('Digite uma lista de números\n')
for a in range(10):
    lista.append(int(input('Digite um numero: ')))
    lista.sort()

novaLista = set(lista)
print('Nova lista sem os números duplicados: ', novaLista)