import numpy as np

def puntofijo(g, x0, Nmax, tol=1.0e-6):
    cont = 1
    x = g(x0)
    e = abs(x-x0)
    while(e>=tol and cont<=Nmax ):
        x0 = x
        x = g(x0)
        e = abs(x-x0)
        cont = cont + 1
    resp = x
    
    if (cont>=Nmax ):
        return ("No hubo convergencia después de {} iteraciones").format(cont)
    return(resp)