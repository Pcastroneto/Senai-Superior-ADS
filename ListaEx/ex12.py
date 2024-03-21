lista = []
verificar = 'Paulo'

print('digite uma lista de nomes\n')
for i in range(5):
    lista.append(str(input('Digite um nome: ')).capitalize())

for a in lista:
    if verificar == a:
        print('O nome está na lista')
    else:
        print('O nome não está na lista')