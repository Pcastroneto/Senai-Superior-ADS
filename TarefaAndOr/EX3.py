#Verifique se uma pessoa é maior ou igual a 18 anos ou se ela tem autorização dos pais.

idade = int(input("Digite a idade da pessoa: "))
autoriza = input("A pessoa tem autorização dos pais? (sim/não): ")

if idade >= 18 or autoriza == "sim":
    print("A pessoa pode participar.")
else:
    print("A pessoa não pode participar.")