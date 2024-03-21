lista = []

while True:
    numeros = int(input("Digite um numero para acrescentar na lista: "))
    lista.append(numeros)
    fim = input("Quer adicionar novos números? Envie 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break
numeros_pares = []
for i in lista:
    if i%2 == 0:
        numeros_pares.append(i)

print('Os numeros pares são:', numeros_pares)