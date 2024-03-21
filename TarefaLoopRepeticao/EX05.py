jair=0
carlos=0
neves=0
nulo=0
branco=0
print('As opcoes são: \n1. Candidato Jair Rodrigues\n2. Candidato Carlos Luz\n3. Candidato Neves Rocha\n4. Nulo\n5. Branco\nEntre com o seu voto:')

while True:
    voto = int(input("insira o número da opção: "))
    if voto == 1:
        jair = jair + 1
    elif voto == 2:
        carlos = carlos + 1
    elif voto == 3:
        neves = neves + 1        
    elif voto == 4:
        nulo = nulo + 1
    elif voto== 5:
        branco = branco + 1
    elif voto == 6:
        break

print('Número de votos do candidato Jair Rodrigues:', jair)
print('Número de votos do candidato Carlos Luz:', carlos)
print('Número de votos do candidato Neves Rocha:', neves)
print('Número de votos Nulos:', nulo,'\nNúmero de votos em Branco:', branco)
if jair > carlos and jair > neves and jair > nulo and jair > branco:
    print('O vencedor foi Jair Rodrigues')
elif carlos > jair  and carlos  > neves  and carlos  >nulo and carlos > branco:
    print('O vencedor foi Carlos Luz')
elif  neves > jair  and neves > carlos  and  neves > nulo and neves > branco:
    print('O vencedor foi Neves Rocha')
else:
    print('Houve um empate ou o numero de nulos e brancos foi maior')
    
