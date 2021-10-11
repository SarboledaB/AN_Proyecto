def raicesmlt(f, df, d2f, x_0, maxiter=50, xtol=1.0e-6, ftol=1.0e-6):
    x = float(x_0) # Se convierte a número de coma flotante
    for i in range(maxiter):
        dx = -f(x) * df(x) / (df(x) ** 2 - f(x) * d2f(x))
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            return x, E, i
    raise RuntimeError("No hubo convergencia después de {} iteraciones").format(maxiter)

def f(x): return x ** 2 - 1

def df(x): return 2 * x

def df(x): return 1

print(raicesmlt(f, df, d2f, 2))