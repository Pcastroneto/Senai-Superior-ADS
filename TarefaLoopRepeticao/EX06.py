p = float(input("Digite o valor inicial que vai depositar: "))

rentabilidade = 0.005

meses = 12

for mes in range(1, meses+1):
    montante = p * (1 + rentabilidade)**mes
    print(f"Montante do mês {mes}: R${montante:.2f}")