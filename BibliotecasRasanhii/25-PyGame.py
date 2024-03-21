'''
É uma biblioteca para desenvolvimento de jogos. 
Ele oferece uma variedade de ferramentas e recursos para o desenvolvimento de jogos, incluindo gráficos, som e entrada do usuário.
'''

import pygame

# Inicializa o PyGame
pygame.init()

# Define as dimensões da janela
window_size = (800, 600)

# Cria a janela
screen = pygame.display.set_mode(window_size)

# Define a cor do retângulo
color = (255, 0, 0)  # vermelho

# Define as coordenadas e dimensões do retângulo
rect = pygame.Rect(50, 50, 100, 100)

# Desenha o retângulo na janela
pygame.draw.rect(screen, color, rect)

# Atualiza a janela
pygame.display.update()

# Aguarda até que o usuário feche a janela
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
