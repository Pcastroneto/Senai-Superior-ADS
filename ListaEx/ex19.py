lista = [1,2,3,4,5,6,7,8,9,10]
novalista = []

print('Escreva uma lista de numeros\n')
numero = int(input('Insira um numero: '))
for i in lista:
    if numero%i == 0:
        novalista.append(i)

print('Os números divisiveis pelo número fornecido pelo usuário são: ', novalista)