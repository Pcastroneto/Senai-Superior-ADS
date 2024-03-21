lista = []

while True:
    numeros = int(input("Insira um numero para acrescentar a lista: "))
    lista.append(numeros)
    fim = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

soma = sum(lista)
quantia = len(lista)
print('A média é: ',soma/quantia)