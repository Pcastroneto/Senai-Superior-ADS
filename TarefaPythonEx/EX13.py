num_lados = int(input("Insira o número de lados do polígono: "))

if num_lados == 3:
    print("TRIÂNGULO")
    lado = float(input("Insira o comprimento do lado: "))
    area = (lado**2 * (3)**0.5) / 4
    print("A área do Triângulo é de:", area)
elif num_lados == 4:
    print("QUADRADO")
    lado = float(input("Insira o comprimento do lado: "))
    area = lado**2
    print("A área do quadrado é de:", area)
elif num_lados == 5:
    print("PENTÁGONO")
else:
    print("Número de lados inválido.")