import numpy as np

def biseccion(f, a, b, Nmax, tol=1.0e-6):
    e=1000
    cont = 1;
    if a > b:
        print("Intervalo mal definido")
    if f(a) * f(b) >= 0.0:
        print("La función debe cambiar de signo en el intervalo")
    if tol <= 0:
        print("La cota de error debe ser un número positivo")
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
    print(x,cont,e)

def f(x):
    return x**5 - 3 * x**2 + 1.6

print(biseccion(f, 1, 1.5, 1000))