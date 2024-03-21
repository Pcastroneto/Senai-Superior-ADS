lista = []

print('Escreva uma lista de numeros\n')
for i in range(10):
    lista.append(int(input('Digite um numero: ')))
    lista.sort()

novaLista = set(lista)
print('nova lista com numeros duplicados removidos: ', novaLista)