
def regla_falsa(f, a, b, Nmax, tol=1.0e-6):
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
    if cont == Nmax:
        return ("No se encontró el intervalo después de {} iteraciones").format(cont)
    return pm
