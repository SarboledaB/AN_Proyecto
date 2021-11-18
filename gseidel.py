import numpy as np

def gauss_seidel (A,b,kMax=50):
    x = np.zeros_like(b)
    n = x.shape[0]
    for k in range(kMax):
        for i in range(n):
            sum = 0
            for j in range(n):
                if j==i:
                    continue
                sum += A[i,j]*x[j]
            x[i] = (b[i]-sum)/A[i,i]
            print(x)
    return x.reshape(-1,1)

n = 5
b = np.random.rand(n)
A = np.identity(n)+np.random.rand(n,n)
x = gauss_seidel(A, b)
print('Are the results accurate?', np.allclose(np.dot(A,x), b.reshape(-1,1)))
                