from py_expression_eval import Parser
import sympy as sp

parser = Parser()

def entrada(func, x_0, Nmax=50, xtol=1.0e-6):
    f = parser.parse(func)
    df = diff(f)
    d2f = diff(df)
    raicesmlt(f, df, d2f, x_0, Nmax, xtol)
    
def diff(f):
    x = sp.Symbol('x')
    df = str(sp.diff(str(f),x))
    return parser.parse(df)

def raicesmlt(f, df, d2f, x_0, Nmax, xtol):
    x = float(x_0) # Se convierte a número de coma flotante
    for cont in range(Nmax):
        dx = -f.evaluate({'x': x}) * df.evaluate({'x': x}) / (df.evaluate({'x': x}) ** 2 - f.evaluate({'x': x}) * d2f.evaluate({'x': x}))
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            return x, E, cont
    return ("No hubo convergencia después de {} iteraciones").format(Nmax)
