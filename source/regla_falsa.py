from py_expression_eval import Parser

parser = Parser()

def entrada(func, a, b, Nmax=1000, tol=1.0e-6):
    f = parser.parse(func)
    return regla_falsa(f, a, b, Nmax, tol)


def regla_falsa(f, a, b, Nmax, tol):
    fa=f.evaluate({'x': a})
    fb=f.evaluate({'x': b})
    pm=(fb*a-fa*b)/(fb-fa)
    fpm=f.evaluate({'x': pm})
    e = abs(b-a) 
    cont=1
    while e>tol and cont<Nmax:
        if fa*fpm<0:
            b=pm 
        else:
            a=pm
        p0=pm
        pm=(f.evaluate({'x': b})*a-f.evaluate({'x': a})*b)/(f.evaluate({'x': b})-f.evaluate({'x': a}))
        fpm=f.evaluate({'x': pm})
        e=abs(pm-p0)
        cont=cont+1
    if cont == Nmax:
        return ("No se encontró el intervalo después de {} iteraciones").format(cont)
    return pm
