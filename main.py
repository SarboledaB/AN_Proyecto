from biseccion import entrada as biseccion
from punto_fijo import entrada as punto_fijo
from regla_falsa import entrada as regla_falsa
from secante import entrada as secante
from busquedas import entrada as busquedas
from raices_multiples import entrada as raices_multiples
from newton import entrada as newton
import numpy as np
import sympy as sp 

from py_expression_eval import Parser

parser = Parser()
    
def diff(f):
    x = sp.Symbol('x')
    df = str(sp.diff(str(f),x))
    return parser.parse(df)

f = parser.parse('x**5 - 3 * x**2 + 1.6')
f2 = parser.parse('x**2 - 1')
df = diff(f)
d2f = diff(df)
gx = parser.parse('exp(-x)')

while True:
    x = input("->")
    if x == '1':
        print(busquedas(f, -1, 0.1))
    elif x == '2':
        print(biseccion(f, -1, 1.5))
    elif x == '3':
        print(raices_multiples(f, -1))
    elif x == '4':
        print(newton(f, -1))
    elif x == '5':
        print(regla_falsa(f, -1, 1.5))
    elif x == '6':
        print(secante(f, -1, 0))
    elif x == '7':
        print(puntofijo(gx, -1))
    else:
        break