x = int(input('Entre com o primeiro número: '))
y = int(input('Entre com o segundo número: '))

if x < y:
    while (x <= y):
        print(x)
        x = x+1
elif x > y:
    while (x>=y):
        print(x)
        x = x-1
else:
    print("Os núemros são iguais")