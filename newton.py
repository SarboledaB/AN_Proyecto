from py_expression_eval import Parser
import sympy as sp 

parser = Parser()

def entrada(func, x_0, Nmax=50, xtol=1.0e-6):
    f = parser.parse(func)
    df = diff(f)
    return newton(f, df, x_0, Nmax, xtol)
    
def diff(f):
    x = sp.Symbol('x')
    df = str(sp.diff(str(f),x))
    return parser.parse(df)

def newton(f, df, x_0, Nmax, xtol):
    x = float(x_0) 
    for i in range(Nmax):
        dx = -f.evaluate({'x': x}) / df.evaluate({'x': x}) 
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            print (x, E, i)
            return x, E, i
    return ("No hubo convergencia después de {} iteraciones").format(Nmax)
