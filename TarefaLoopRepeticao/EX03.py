#3 - Faça um programa que peça ao usuário para digitar uma sequência de números inteiros.
#O programa deve imprimir a soma dos números digitados, mas parar a soma se o usuário digitar um número negativo.
# leia o valor de n

resul = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0:
        break
    resul += n

print('A soma dos números inseridos é de:', resul)