lista = []

print('Insira uma lista de números\n')
for i in range(5):
    numero = int(input('digite um numero: '))
    if numero %2 == 1:
        lista.append(numero)

print('A soma dos numeros impares da lista é igual: ', sum(lista))