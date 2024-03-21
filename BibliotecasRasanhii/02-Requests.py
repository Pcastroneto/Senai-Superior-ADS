'''
A biblioteca 'Requests' permite que o dev faça uma solicitação ou requisição em uma base ou conjunto de dados.
Ela é formada por quatro principais métodos: Get, Post, Patch e Delete. Assim é essencial para estabelecer a interação entre uma base e uma aplicação.

'''

import requests

print('Digite a URL que deseja estabeler uma conexão.')
url = input('URL: ')

try:
    response = requests.get(url)
    response.raise_for_status()
    print("Conexão bem sucedida!")
    
except requests.exceptions.HTTPError as http_err:
    print(f"Erro HTTP: {http_err}")
    
except Exception as err:
    print(f"Erro: {err}")