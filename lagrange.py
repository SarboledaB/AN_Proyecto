'''%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de Lagrange

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%L, polinomios de Lagrange
%Coef, coeficientes del polinomio de interpolaci�n'''
import numpy as np

def lagrange(x,y):

    #%Inicializaci�n
    n=len(x);
    L= np.zeros(n);

    #%Ciclo
    for i in range(n):
        aux0 = np.setdiff(x,x(i));
        aux=[1 -aux0(1)];
        for j in range(n-1):
            aux = np.conv(aux,[1 -aux0(j)])
        
        L(i,)=aux/np.polyval(aux,x(i))


    #%Entrega de resultados
    Coef=y*L;
    
    return Coef
    