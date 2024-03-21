lados = int(input("Informe o número de lados do polígono: "))

if lados < 3:
    print("NÃO É UM POLÍGONO")
elif lados == 3:
    print("TRIÂNGULO")
    area = (lados**2 * (3**0.5)) / 4
    print("A área do triângulo é de", area)
elif lados == 4:
    print("QUADRADO")
    area = lados**2
    print("A área do quadrado é de", area)
elif lados == 5:
    print("PENTÁGONO")
else:
    print("POLÍGONO NÃO IDENTIFICADO")