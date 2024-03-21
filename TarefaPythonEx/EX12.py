altura = float(input("Digite sua altura: "))
sexo = int(input("Digite seu sexo (1 para feminino e 2 para masculino): "))

if sexo == 1:
    peso_ideal = 62.1 * altura - 44.7
    print("O seu peso ideal é: ", peso_ideal)

elif sexo == 2:
    peso_ideal = 72.7 * altura - 58
    print("O seu peso ideal é: ", peso_ideal)

else:
    print("Sexo inválido.")