from py_expression_eval import Parser

parser = Parser()

def entrada(func, x0, Nmax=1000, tol=1.0e-6):
    g = parser.parse(func)
    return puntofijo(g, x0, Nmax, tol)
    print(func, x0, Nmax, tol)

def puntofijo(g, x0, Nmax, tol):
    cont = 1
    x = g.evaluate({'x': x0})
    e = abs(x-x0)
    while(e>=tol and cont<=Nmax ):
        x0 = x
        x = g.evaluate({'x': x0})
        e = abs(x-x0)
        cont = cont + 1
    resp = x
    
    if (cont>=Nmax ):
        return ("No hubo convergencia después de {} iteraciones").format(cont)
    return(resp)