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

def vandermonde (x,y, num_puntos=100):

    #Inicializacion
    n = len(x)
    A = np.zeros((n,n))

    #Ciclo
    for i in range(n):
        A[:,i]=(x**(n-i-1))


    #Entrega de resultados
    Coef = np.linalg.solve(A,y)
    
    f = ""
    for i in range(len(Coef)):
        f += '+'+str(Coef[i])+'*x**'+str(len(Coef)-i-1)
    f = parser.parse(f)

    xr = np.linspace(-np.pi, np.pi, num_puntos)
    yr = np.array([f.evaluate({'x': i}) for i in xr])
    # Gráfica
    plt.style.use('ggplot')
    plt.plot(xr, yr)
    plt.scatter(x, y)
    plt.legend(['Lagrange', 'Datos'], loc='best')
    return Coef
    plt.show()