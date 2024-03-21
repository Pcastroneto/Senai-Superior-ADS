lista = []

print('Digite uma lista de números!\n')

for i in range(5):
    numero = int(input('Digite um número: '))
    if numero < 5:
        lista.append(numero)
print('Os numeros menores que 5 são os: ',lista)