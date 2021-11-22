'''Este programa halla el polinomio interpolante de los datos dados usando el
m�todo de Vandermonde

Entradas: 
X, abscisas 
Y, ordenadas

Salidas
Coef, coeficientes del polinomio'''

import numpy as np

def vandermonde (x,y):

    #Inicializacion
    n = len(x)
    A = np.zeros(n)

    #Ciclo
    for i in range(n) :
        A(0,i)=(x**(n-i))


    #Entrega de resultados
    Coef = A/y
    
    return Coef
    
