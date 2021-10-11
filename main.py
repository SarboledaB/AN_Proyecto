from biseccion import biseccion
from punto_fijo import puntofijo
from regla_falsa import regla_falsa
from secante import secante
from busquedas import busquedas
from raices_multiples import raicesmlt
from newton import newton
import numpy as np

def f(x):
    return x**5 - 3 * x**2 + 1.6

def f2(x): return x ** 2 - 1

def df(x): return 5 * x**4 - 6 * x

def d2f(x): return 20 * x**3 - 6


gx = lambda x: np.exp(-x)

while True:
    x = input("->")
    if x == '1':
        print(busquedas(f, -1, 0.1, 1000))
    elif x == '2':
        print(biseccion(f, -1, 1.5, 1000))
    elif x == '3':
        print(raicesmlt(f, df, d2f, -1))
    elif x == '4':
        print(newton(f, df, -1))
    elif x == '5':
        print(regla_falsa(f, -1, 1.5, 1000))
    elif x == '6':
        print(secante(f, -1, 0, 1000))
    elif x == '7':
        print(puntofijo(gx, -1, 1000))
    else:
        break