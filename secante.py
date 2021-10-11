
def secante(f, x0, x1, Nmax, tol=1.0e-6):
    f0=f(x0)
    f1=f(x1)
    e = abs(x1-x0) 
    cont=1
    while e>tol and cont<Nmax:
        xact=x1-f1*(x1-x0)/(f1-f0)
        fact=f(xact)
        e=abs(xact-x1)
        cont=cont+1 
        x0=x1
        f0=f1
        x1=xact
        f1=fact
    return x1


def f(x):
    return x**5 - 3 * x**2 + 1.6

print(secante(f, 1, 1.5, 1000))