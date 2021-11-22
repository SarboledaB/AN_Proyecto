import numpy as np
from py_expression_eval import Parser

parser = Parser()

def entrada(func, a, b, Nmax=1000, tol=1.0e-6):
    f = parser.parse(func)
    biseccion(f, a, b, Nmax, tol)

def biseccion(f, a, b, Nmax, tol):
    e=1000
    cont = 1;
    if a > b:
        print ("Intervalo mal definido")
        return ("Intervalo mal definido")
    if f.evaluate({'x': a}) * f.evaluate({'x': b}) >= 0.0:
        print ("La función debe cambiar de signo en el intervalo")
        return ("La función debe cambiar de signo en el intervalo")
    x = (a + b) / 2.0
    while cont<Nmax:
        if b - a < tol:
            print (x)
            return x
        elif np.sign(f.evaluate({'x': a})) * np.sign(f.evaluate({'x': x})) > 0:
            a = x
        else:
            b = x
        x = (a + b) / 2.0
        cont=cont+1;
    if cont == Nmax:
        print ("No hubo convergencia después de {} iteraciones").format(cont)
        return ("No hubo convergencia después de {} iteraciones").format(cont)