#Escreva um código que verifique se uma pessoa é alfabetizada (sabe ler e escrever) e tem mais de 25 anos de idade.
idade = int(input("Digite a idade da pessoa: "))
alfabetizada = input("A pessoa é alfabetizada? (sim/não): ")

if idade > 25 and alfabetizada == "sim":
    print("A pessoa é alfabetizada e tem mais de 25 anos.")
else:
    print("A pessoa não atende aos requisitos.")