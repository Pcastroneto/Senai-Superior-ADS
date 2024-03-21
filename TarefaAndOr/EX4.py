#Escreva um código que verifique se um número é par ou divisível por 3.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
elif numero % 3 == 0:
    print("O número é divisível por 3")
else:
    print("O número não é par e nem divisível por 3")