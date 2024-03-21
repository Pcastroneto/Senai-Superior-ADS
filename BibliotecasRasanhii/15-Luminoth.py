'''
Luminoth é uma biblioteca de visão computacional open source, que permite a construção e treinamento de modelos de detecção de objetos, classificação de imagens e segmentação semântica.
Exemplo:


from luminoth import Detector, read_image

# Inicializa o modelo de detecção de objetos
detector = Detector()

# Lê uma imagem
image = read_image('/path/to/image.jpg')

# Executa a detecção de objetos na imagem
predictions = detector.predict(image)

# Exibe as previsões
print(predictions)
'''