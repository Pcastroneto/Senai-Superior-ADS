'''
É uma biblioteca Python para análise de dados HTML e XML. 
Ela permite que os usuários analisem e naveguem em documentos HTML e XML e extraiam informações relevantes, como tags e atributos.
'''

from bs4 import BeautifulSoup
import requests

# Faz a requisição para o site desejado
page = requests.get("https://www.python.org/")

# Cria um objeto BeautifulSoup com o conteúdo da página
soup = BeautifulSoup(page.content, "html.parser")

# Encontra todos os links da página e imprime seus textos e URLs
for link in soup.find_all("a"):
    print(link.text.strip(), "=>", link.get("href"))
