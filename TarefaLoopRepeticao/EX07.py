num = int(input("Fatorial de: ") )

resultado=1
conta=1

while conta <= num:
    resultado *= conta
    conta += 1

print('O resultado é', resultado)