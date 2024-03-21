'''

'''

import mahotas as mh
import matplotlib.pyplot as plt

# Carrega a imagem
im = mh.imread('/home/ec2-user/environment/estudo_das_bibliotecas/designe.jpg')

# Mostra a imagem
plt.imshow(im, cmap='gray')
plt.show()
