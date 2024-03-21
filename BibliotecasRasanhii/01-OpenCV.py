"""

O OpenCV é uma biblioteca de processamento de imagens que permite a criação de aplicativos de visão computacional com suporte para diversos sistemas operacionais. 
Essa biblioteca é open source (código aberto) e pode ser usada para análise de imagens.

"""

import cv2


# carrega a imagem em uma variável
imagem = cv2.imread('/home/ec2-user/environment/estudo_das_bibliotecas/designe.jpg')

# verifica se a imagem foi carregada corretamente
if imagem is None:
    print('Não foi possível carregar a imagem')
else:
    print(imagem.shape) # verifica as dimensões da imagem

# exibe a imagem
cv2.imshow('Imagem Original', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
