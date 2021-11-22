'''%Este programa halla el polinomio interpolante de los datos dados usando el
%m�todo de diferencias divididas

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%Coef, coeficientes del polinomio de Newton'''
import numpy as np
def C20_difdivididas(X,Y):

    #%Inicializaci�n
    n=len(X)
    D=np.zeros(n)

    #%Ciclo
    D(0,1)=Y
    i = 2
    for i in range(n):
        aux0=D(i-1,n,i-1);
        aux=np.diff(aux0);
        aux2=X(i,n)-X(1,n-i+1);
        D(i,n,i)=aux/aux2
    

    #%Entrega de resultados
    Coef=np.diag(D)
    return Coef