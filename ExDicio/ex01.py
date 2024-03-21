lista = {}

def numeros():
    return str(input('Digite o nome do item: '))

while True:
    item = numeros()
    if item == '':
        break
    valor = int(input('Informe agora o valor do item: '))
    lista[item] = valor

maxi = max(lista.items())
print('O maior valor da lista é: ', maxi)