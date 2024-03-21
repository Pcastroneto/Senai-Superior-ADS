lista = []

while True:
    numero = input("Digite um número para acrescentar na lista: ")
    lista.append(numero)
    fim = input("Quer inserir novos números? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

maximo = max(lista)
minimo = min(lista)

print("O número máximo é:",maximo)
print("O número mínimo é:",minimo)