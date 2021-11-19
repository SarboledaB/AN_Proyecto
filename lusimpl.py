import numpy as np
from sustregr import sustregr
from sustprgr import sustprgr

def lusimpl(A, b):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n,n))
    M = A.astype(float)
    
    for i in range(n-1):
        for j in range(i+1,n):
            if M[j,i] != 0:
                L[j,i]=M[j,i]/M[i,i]
                M[j,i:n]=M[j,i:n]-(M[j,i]/M[i,i])*M[i,i:n]
        U[i,i:n]=M[i,i:n];
        U[i+1,i+1:n]=M[i+1,i+1:n]

    U[n-1,n-1]=M[n-1,n-1]
    
    print(L)
    print(U)
    L = np.insert(L, L.shape[0],b,axis=1).astype(float)
    z = sustprgr(L)
    U = np.insert(U, U.shape[0],z,axis=1).astype(float)
    x = sustregr(U)
    
    return x
    
a = np.array([[3,5,4],
              [1,1,-1],
              [2,3,1]])
b = np.array([2,1,1])

print(lusimpl(a,b))