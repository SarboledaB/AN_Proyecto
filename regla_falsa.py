
def secante(f, a, b, Nmax, tol=1.0e-6):
    fa=f(a)
    fb=f(b)
    pm=(fb*a-fa*b)/(fb-fa)
    fpm=f(pm)
    e = abs(b-a) 
    cont=1
    while e>tol and cont<Nmax:
        if fa*fpm<0:
            b=pm 
        else:
            a=pm
        p0=pm
        pm=(f(b)*a-f(a)*b)/(f(b)-f(a))
        fpm=f(pm)
        e=abs(pm-p0)
        cont=cont+1
    return pm


def f(x):
    return x**5 - 3 * x**2 + 1.6

print(secante(f, 1, 1.5, 1000))