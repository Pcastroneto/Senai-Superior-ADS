lista = []

print('Digite uma lista de números\n')
for i in range(5):
    lista.append(int(input('Digite um número: ')))
    lista.sort()
print('O segundo número mais alto na lista é: ', lista[-2])