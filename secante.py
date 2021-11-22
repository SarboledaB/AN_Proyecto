from py_expression_eval import Parser

parser = Parser()

def entrada(func, x0, x1, Nmax=1000, tol=1.0e-6):
    f = parser.parse(func)
    return secante(f, x0, x1, Nmax, tol)

def secante(f, x0, x1, Nmax, tol=1.0e-6):
    f0=f.evaluate({'x': x0})
    f1=f.evaluate({'x': x1})
    e = 1000
    cont=1
    while e>tol and cont<Nmax:
        xact=x1-f1*(x1-x0)/(f1-f0)
        fact=f.evaluate({'x': xact})
        e=abs(xact-x1)
        cont=cont+1 
        x0=x1
        f0=f1
        x1=xact
        f1=fact
    if cont == Nmax:
        return ("No se encontró el intervalo después de {} iteraciones").format(cont)
    return x1