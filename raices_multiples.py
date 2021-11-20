from py_expression_eval import Parser

parser = Parser()

def entrada(func, x_0, Nmax=50, xtol=1.0e-6, ftol=1.0e-6):
    f = parser.parse(func)
    df = diff(f)
    d2f = diff(df)
    raicesmlt(f, df, d2f, x_0, Nmax, xtol, ftol)

def raicesmlt(f, df, d2f, x_0, Nmax, xtol, ftol):
    x = float(x_0) # Se convierte a número de coma flotante
    for cont in range(Nmax):
        dx = -f.evaluate({'x': x}) * df.evaluate({'x': x}) / (df.evaluate({'x': x}) ** 2 - f.evaluate({'x': x}) * d2f.evaluate({'x': x}))
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            return x, E, cont
    return ("No hubo convergencia después de {} iteraciones").format(Nmax)
