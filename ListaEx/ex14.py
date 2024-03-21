lista = []

print('Digite uma lista de números\n')
for i in range(5):
    lista.append(int(input('Digite um número: ')))
    lista.sort(reverse = True)
print('O segundo menor número na lista é o: ', lista[-2])