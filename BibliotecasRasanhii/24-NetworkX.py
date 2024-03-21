'''
Uma biblioteca Python para análise de redes complexas. 
Ele permite que os usuários construam, visualizem e analisem redes complexas, 
incluindo redes sociais, redes de transporte e redes biológicas.
'''

import networkx as nx

# Criando um grafo
G = nx.Graph()

# Adicionando nós ao grafo
G.add_node(1)
G.add_node(2)
G.add_node(3)

# Adicionando arestas ao grafo
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 1)

# Imprimindo o grafo
print(G.nodes())
print(G.edges())
