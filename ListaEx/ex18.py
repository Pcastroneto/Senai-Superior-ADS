lista = []

print('Digite uma lista de números\n')
for i in range(10):
    numero = int(input('Insira um número: '))
    if numero%3 == 0:
        lista.append(numero)

print('Apeanas os números divisiveis por 3 são: ', lista)