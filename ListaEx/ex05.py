lista = []

while True:
    numeros = int(input("Insira um numero para acrescentar a lista: "))
    lista.append(numeros)
    end = input("Deseja inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if end.lower() == 'n':
        break

ordem= sorted(lista)
print(ordem)