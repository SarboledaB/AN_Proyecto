def newton(f, df, x_0, Nmax=50, xtol=1.0e-6, ftol=1.0e-6):
    x = float(x_0) 
    for i in range(Nmax):
        dx = -f(x) / df(x) 
        x = x + dx
        E = abs(dx / x)
        if E < xtol:
            return x, E, i
    return ("No hubo convergencia después de {} iteraciones").format(Nmax)
