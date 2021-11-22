'''%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de Lagrange

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%L, polinomios de Lagrange
%Coef, coeficientes del polinomio de interpolaci�n'''
import numpy as np
import sympy
import matplotlib.pyplot as plt

from py_expression_eval import Parser

parser = Parser()

def lagrange(x,y,num_puntos=100):
    #%Inicializaci�n
    n=len(x)
    L= np.zeros((n,n))

    #%Ciclo
    for i in range(n):
        aux0 = np.setdiff1d(x,x[i]);
        aux=np.array([1, -aux0[0]]);
        for j in range(1,n-1):
            aux = np.convolve(aux,[1, -aux0[j]],mode='full')
        
        L[i,:]=aux/np.polyval(aux,x[i])


    #%Entrega de resultados
    pol=np.dot(y,L);
    f = ""
    for i in range(len(pol)):
        f += '+'+str(pol[i])+'*x**'+str(len(pol)-i-1)
    f = parser.parse(f)

    xr = np.linspace(-np.pi, np.pi, num_puntos)
    yr = np.array([f.evaluate({'x': i}) for i in xr])
    # Gráfica
    plt.style.use('ggplot')
    plt.plot(xr, yr)
    plt.scatter(x, y)
    plt.legend(['Lagrange', 'Datos'], loc='best')
    plt.show()
    
    return pol
