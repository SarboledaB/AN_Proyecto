from py_expression_eval import Parser

def entrada(func, x_0, Nmax=50, xtol=1.0e-6, ftol=1.0e-6):
    f = parser.parse(func)
    df = diff(f)
    newton(f, df, x_0, Nmax, xtol, ftol)

def newton(f, df, x_0, Nmax, xtol, ftol):
    x = float(x_0) 
    for i in range(Nmax):
        dx = -f.evaluate({'x': x}) / df.evaluate({'x': x}) 
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            return x, E, i
    return ("No hubo convergencia después de {} iteraciones").format(Nmax)
