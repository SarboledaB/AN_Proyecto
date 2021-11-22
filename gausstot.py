import numpy as np
from sustregr import sustregr

def gausspar(A, b):
    n = A.shape[0]
    M = np.insert(A, A.shape[0],b,axis=1).astype(float)
    camb = []
    for i in range(0,n-1):
        [a,b] = np.where(np.abs(M)==np.max(np.abs(M[i:,i:n])))

        if b[0] != i:
            M[:,[i,b[0]]]=M[:,[b[0],i]]
            camb.append([i,b[0]])
        
        if a[0] != i:
            M[[i,a[0]],:]=M[[a[0],i],:]
            
        for j in range(i+1,n):
            if M[j,i] != 0:
                M[j,i:n+1]=M[j,i:n+1]-(M[j,i]/M[i,i])*M[i,i:n+1]
    x = sustregr(M) 
    for i in range(len(camb)-1,-1,-1):
        x[[camb[i][0],camb[i][1]]]=x[[camb[i][1],camb[i][0]]]
        
    return x
    
# a = np.array([[2,3,1],
#               [3,5,4],
#               [1,1,-1]])
# b = np.array([1,2,1])

# print(gausspar(a,b))