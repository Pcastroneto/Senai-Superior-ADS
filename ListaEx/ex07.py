lista = []

while True:
    nomes = input("Insira um nome para a lista: ")
    lista.append(nomes)
    fim = input("Deseja inserir novos nomes? Digite 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break

maior_palavra = ""
menor_palavra = lista[0]
zero = 0
for i in lista:
    if len(i) > len(maior_palavra):
        maior_palavra = i
    if len(i) < len(menor_palavra):
        menor_palavra = i

print('O nome mais longo é:',maior_palavra)
print('O nome mais curto é:',menor_palavra)