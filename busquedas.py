def f(x):
    return 1

def busquedas(f, x0, h, Nmax):
    """Método de busquedas
    Halla un intervalo donde f(x) tiene un cambio de signo usando el método
    de búsquedas incrementales
    Argumentos
    ----------
    f - Función, debe ser continua
    x0 - Punto inicial
    h - Paso
    Nmax - Número máximo de iteraciones
    Devuelve
    --------
    a - Extremo izquierdo del intervalo
    b - Extremo derecho del intervalo
    i, Número de iteraciones
    """
    xant = float(x0)
    fant = f(xant)
    xact = xant + h
    fact = f(xact)
    i = 0

    while i<Nmax:
        if fant*fact<0:
            break
        xant=xact
        fant=fact
        xact=xant+h
        fact=f(xact)
        i += 1
    if i == Nmax:
        return ("No hubo convergencia después de {} iteraciones").format(i)

    return xant, xact, i

print(busquedas(f, -1.0, 0.1, 1000))