lista = []

print('Digite uma lista de números\n')

for i in range(5):
    numero = int(input('Digite um número: '))
    if numero > 10:
        lista.append(numero)
print('Os numeros maiores que 10 são os: ',lista)