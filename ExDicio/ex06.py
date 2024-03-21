dicio = {'paulo':'00','anderson':'01', 'junior':'03', 'roberto':'04'}

def ordenando_chaves(dicio):
    chaves_ordem = sorted(dicio.keys())
    lista_ordenada = [(chave, dicio[chave]) for chave in chaves_ordem]
    print(lista_ordenada)

        
ordenando_chaves(dicio)