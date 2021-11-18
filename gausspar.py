import numpy as np
from sustregr import sustregr

def gausspar(A, b):
    n = a.shape[0]
    M = np.insert(A, A.shape[0],b,axis=1).astype(float)
    for i in range(0,n-1):
        if(np.max(M[i:,i])!=M[i,i]):    # Si el coeficiente actual no es el valor máximo, pivote de columna
            temp_i=int(np.where(M==np.max(M[i:,i]))[0]) #temp_i es el índice de fila donde se encuentra el valor máximo
            M[[i,temp_i],:]=M[[temp_i,i],:] #intercambiar
             
        for j in range(i+1,n):
            if M[j,i] != 0:
                M[j,i:n+1]=M[j,i:n+1]-(M[j,i]/M[i,i])*M[i,i:n+1]
    return sustregr(M) 
    
a = np.array([[3,2,1],
              [5,3,4],
              [1,1,-1]])
b = np.array([1,2,1])

print(gausspar(a,b))