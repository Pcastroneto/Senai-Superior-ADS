lista = {}

def inserirNome():
    return str(input('Insira o nome: '))
def inserirIdade():
    return int(input('Insira a idade: '))

while True:
    nome = inserirNome()
    if nome == '':
        break

    idade = inserirIdade()
    lista[nome] = {
        'idade': idade
    }

for i, d in lista.items():
    if d['idade'] > 18:
        print('nome:', i ,'idade:', d['idade'])