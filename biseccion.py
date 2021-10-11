import numpy as np

def biseccion(f, a, b, Nmax, tol=1.0e-6):
    e=1000
    cont = 1;
    if a > b:
        return ("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        return ("La función debe cambiar de signo en el intervalo")
    x = (a + b) / 2.0
    while cont<Nmax:
        if b - a < tol:
            return x
        elif np.sign(f(a)) * np.sign(f(x)) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0
        cont=cont+1;
    if cont == Nmax:
        return ("No hubo convergencia después de {} iteraciones").format(cont)