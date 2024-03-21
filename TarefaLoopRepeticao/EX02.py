#Faça um programa que peça ao usuário para adivinhar um número entre 1 e 100.
#Enquanto o número digitado não for igual a um número secreto definido pelo programa,
#o programa deve pedir ao usuário que tente novamente. Quando o usuário acertar o número,
#o programa deve imprimir "Parabéns, você acertou!".
#Use a biblioteca abaixo para números aleatórios:
#import random
#numero_secreto = random.randint(1, 100)


import random
def gerador():
    return random.randint(1,100)

def jogo():
    resposta = gerador()
    print("\nAdivinhe o número!")

    palpite=0
    while palpite is not resposta:
        palpite = int(input("Qual seu palpite: "))
        if palpite > resposta:
            print("Errou! Tente um número menor que ", palpite)
        elif palpite < resposta:
            print("Errou! Tente um númemro maior que ",palpite)
        else:
            print("Você conseguiu! O número gerado foi ",resposta)
    
while True:
    jogo()