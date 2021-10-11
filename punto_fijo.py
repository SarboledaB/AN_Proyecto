import numpy as np

def puntofijo(g, x0, Nmax, tol=1.0e-6):
    acum = 1
    x = g(x0)
    e = abs(x-x0)
    while(e>=tol and acum<=Nmax ):
        x0 = x
        x = g(x0)
        e = abs(x-x0)
        acum = acum + 1
    resp = x
    
    if (acum>=Nmax ):
        resp = np.nan
    return(resp)

gx = lambda x: np.exp(-x)

print(puntofijo( gx, 0.2, 1000, 0.001 ))

