'''Este programa halla el polinomio interpolante de los datos dados usando el
m�todo de Vandermonde

Entradas: 
X, abscisas 
Y, ordenadas

Salidas
Coef, coeficientes del polinomio'''

import numpy as np
import matplotlib.pyplot as plt

from py_expression_eval import Parser

parser = Parser()

def vandermonde (x,y):

    #Inicializacion
    n = len(x)
    A = np.zeros((n,n))

    #Ciclo
    for i in range(n):
        A[:,i]=(x**(n-i-1))


    #Entrega de resultados
    Coef = np.linalg.solve(A,y)
    
    return Coef
    
# # Datos
# x = np.linspace(-np.pi, np.pi, 4)
# y = np.array([np.sin(i) for i in x])
# pol = vandermonde(x, y)
# print(pol)
# f = '{}*x**3 + {}*x**2 + {}*x**1 + {}'.format(pol[0],pol[1],pol[2],pol[3])
# f = parser.parse(f)

# xr = np.linspace(-np.pi, np.pi, 10)
# yr = np.array([f.evaluate({'x': i}) for i in xr])


# # Gráfica
# plt.style.use('ggplot')
# plt.plot(xr, yr)
# plt.scatter(x, y)
# plt.legend(['Lagrange', 'Datos'], loc='best')
# plt.show()