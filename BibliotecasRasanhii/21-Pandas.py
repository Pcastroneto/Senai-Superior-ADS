'''
Muito conhecida, o Pandas é uma biblioteca para manipulação e análise de dados. 
Ela oferece uma estrutura de dados flexível e poderosa para a manipulação de dados tabulares e operações de agregação e análise de dados.
'''

import pandas as pd

# Lendo um arquivo CSV e armazenando os dados em um DataFrame do Pandas
df = pd.read_csv('/home/ec2-user/environment/estudo_das_bibliotecas/100-Best-Movies-on-Netflix.csv')

# Exibindo as primeiras 5 linhas do DataFrame
print(df.head())

"""
# Exibindo a média da coluna 'idade'
print('Média de idade:', df['idade'].mean())

# Exibindo a quantidade de pessoas de cada sexo
print('Quantidade de homens e mulheres:')
print(df['sexo'].value_counts())
"""