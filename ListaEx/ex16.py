lista = []

print('Digite uma lista de números\n')

for a in range(10):
    lista.append(int(input('Digite um número: ')))
 
novalista = [x for a, x in enumerate(lista) if a != lista.index(x)]
print('Nova lista somente com os números duplicados: ', novalista)