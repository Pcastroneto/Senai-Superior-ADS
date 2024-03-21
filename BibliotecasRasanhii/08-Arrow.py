'''
Arrow é uma biblioteca que oferece uma abordagem sensível e amigável para criar, manipular, formatar e converter datas, horários e carimbos de data/hora. 
Ele implementa e atualiza o tipo datetime, preenchendo lacunas na funcionalidade e fornecendo uma API de módulos inteligente que oferece suporte a muitos cenários de criação comuns.

'''

import arrow

# Criando um objeto Arrow com a data e hora atuais
agr = arrow.now()

# Imprimindo a data e hora formatadas
print(agr.format('DD/MM/YYYY HH:mm:ss'))

# Adicionando 2 horas ao objeto Arrow
duas_horas_atras = agr.shift(hours=2)

# Calculando a diferença entre os objetos Arrow em minutos
difere = (duas_horas_atras - agr).total_seconds() / 60

# Imprimindo a diferença em minutos
print(f'A diferença entre {agr} e {duas_horas_atras} é de {difere:.2f} minutos')
