'''
A Scikit Learn é uma biblioteca para aprendizado de máquina e mineração de dados. 
Ela oferece uma ampla gama de algoritmos de aprendizado de máquina para tarefas como classificação, 
regressão e agrupamento, bem como ferramentas para pré-processamento de dados e avaliação de modelos.
Exemplo:


from sklearn.linear_model import LinearRegression

# Dados de treinamento
X_train = [[1, 1000], [2, 1500], [3, 2000], [4, 2500], [5, 3000]]
y_train = [50000, 75000, 100000, 125000, 150000]

# Cria o modelo de regressão linear
model = LinearRegression()

# Treina o modelo
model.fit(X_train, y_train)

# Dados de teste
X_test = [[3, 1800], [4, 2200]]

# Faz as predições
y_pred = model.predict(X_test)

# Imprime as predições
for i in range(len(X_test)):
    print(f"Preço previsto para uma casa com {X_test[i][0]} quartos e área de {X_test[i][1]}: {y_pred[i]}")


Um código simples que utiliza o algoritmo de Regressão Linear para prever o preço de uma casa com base em duas características:
 número de quartos e área total.
'''
