dicionario = {}

def cria_dicionario():
    while True:
        chave = input('Digite uma chave (ou digite "end"): ')
        if chave == '' or chave == 'end':
            break
        valor = int(input('Digite um número para a chave: '))
        if valor == '' or chave == 'end':
            break
        dicionario[chave] = valor
        
    print(dicionario)
    
cria_dicionario()