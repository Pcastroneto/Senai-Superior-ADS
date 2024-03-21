valor=int(input("Digite um valor de 1 a 10: "))

if valor <= 10 and valor >= 1:
    for i in range(10):
        print("%d x %d = %d" % (valor, i+1, valor*(i+1)) )
else:
    print("O valor não está entre 1 a 0")
