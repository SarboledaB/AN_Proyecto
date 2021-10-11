from biseccion import biseccion
from punto_fijo import puntofijo
from regla_falsa import regla_falsa
from secante import secante
import numpy as np

def f(x):
    return x**5 - 3 * x**2 + 1.6

gx = lambda x: np.exp(-x)

while True:
    x = input("->")
    if x == '1':
        pass
    elif x == '2':
        print(biseccion(f, 1, 1.5, 1000))
    elif x == '3':
        pass
    elif x == '4':
        pass
    elif x == '5':
        print(regla_falsa(f, 1, 1.5, 1000))
    elif x == '6':
        print(secante(f, 1, 1.5, 1000))
    elif x == '7':
        print(puntofijo( gx, 0.2, 1000, 0.001 ))
    else:
        break