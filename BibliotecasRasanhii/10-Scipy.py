'''

Um exemplo:


import numpy as np
from scipy.optimize import minimize

# Definindo a função objetivo
def rosen(x):
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

# Definindo a condição de restrição
cons = ({'type': 'ineq', 'fun': lambda x: np.array([1 - sum(x)])})

# Definindo o ponto inicial
x0 = np.zeros(10)

# Minimizando a função com restrição utilizando o método SLSQP
res = minimize(rosen, x0, method='SLSQP', constraints=cons)

# Imprimindo o resultado
print(res)


Neste exemplo, estamos utilizando a função rosen como função objetivo e a condição de restrição cons. 
Em seguida, definimos o ponto inicial x0 e utilizamos o método minimize da biblioteca Scipy para minimizar a função com restrição utilizando o método SLSQP. 
Por fim, imprimimos o resultado obtido.
'''