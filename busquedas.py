
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
    cont, Número de iteraciones
    """
    xant = float(x0)
    fant = f(xant)
    xact = xant + h
    fact = f(xact)
    cont = 0

    while cont<Nmax:
        if fant*fact<0:
            break
        xant=xact
        fant=fact
        xact=xant+h
        fact=f(xact)
        cont += 1
    if cont == Nmax:
        return ("No se encontró el intervalo después de {} iteraciones").format(cont)

    return xant, xact, cont
