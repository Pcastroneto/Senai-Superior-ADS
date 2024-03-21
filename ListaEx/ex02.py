lista = []

while True:
    palavras = input("Digite uma palavra para acrescentar na lista: ")
    lista.append(palavras)
    fim = input("Quer adicionar novas palavras? Envie 's' para sim ou 'n' para não: ")
    if fim.lower() == 'n':
        break
    
novaLista = []
for i in lista:
    if i[0] == 'a':
        novaLista.append(i)

print('As palavras que começam com "a" são:',novaLista)