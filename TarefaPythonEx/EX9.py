a1 = int(input("Digite o valor inicial (a1): "))
n = int(input("Digite a quantidade de termos (n): "))
q = int(input("Digite a razão (q) [q >= 2]: "))

if q >= 2:
    Sn = a1 * (q**n - 1) / (q - 1)
    print("A soma dos termos da PA é:", Sn)
else:
    print("A razão (q) deve ser maior ou igual a 2.")