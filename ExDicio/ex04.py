dicionario = {}

def criando_dicionario():
    while True:
        Chave = input('Insira uma chave (ou digite "finalizar"): ')
        if Chave == '' or Chave == 'finalizar':
            break
        valor = int(input('Insira um número para a chave: '))
        if valor == '' or Chave == 'finalizar':
            break
        dicionario[Chave] = valor
        
        
    for i in dicionario.keys():
        print(f'As chaves são: {i}' )
    for i in dicionario.keys():
        print(f'Os valores são: {dicionario[i]}')
    
criando_dicionario()