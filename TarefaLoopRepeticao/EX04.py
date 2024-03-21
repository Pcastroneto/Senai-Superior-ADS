import random
resultado = random.randint(0, 1)

lancamentos = int(input('Digite o número de quantas vezes quer jogar a moeda: '))

cara = 0
coroa = 0
for i in range(lancamentos):
    if resultado % 2 == 0:
        print('Cara')
        cara += 1
    else:
        print('Coroa')
        coroa += 1

print('Número total de caras:', cara , '\nNúmero total de coroas:',coroa )