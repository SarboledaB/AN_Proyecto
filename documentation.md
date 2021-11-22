# Documentation

![Alt text](images\ANumerico.drawio.png?raw=true "Optional Title")


## Numerical solution of nonlinear equations.

### Incremental searches.
Given f (x) = 0, we apply the following steps:

- The continuity of f must be guaranteed with arguments
theoretical.
- We choose a starting value x0 and a 4x that expresses the
size of the interval that we want to find.
- We generate a sequence x0, x1, ..., xn such that
xn = xn − 1 + 4x.
- Each time a value of xn is generated, we find the value of f (xn).
- We observe the signs of f (xn) and f (xn − 1).
- We suspend the process when there is a change of
sign at f (xn) and f (xn − 1) or when we reach a limit of
iterations without finding said change.

```bash
In x0, x1, inc
out table c

count = 0
while a<=b
    c = a + inc
    if function(a)*function(c) then
        count = count + 1
        print table (cont, 1) = a
        print table (cont, 2) = c 
        a = c
    else
        a = c
    end if

    if function(c) == c then
        print "Hay una raiz en c"
    end if
end while
``` 
        
### Bisection.
The method is quite simple, all it does is divide the
interval in the middle and check which side the root was to get a new interval.

```bash
in Xi, Xs, tol, Iter
Yi = f(Xi)
Ys = f(Xs)
if Yi = 0 then
    print ‘Xi is a root’
else
    if Ys = 0 then
        print ‘Xs is a root’
    else
        if Yi*Ys < 0 then
            Xm= (Xi + Xs)/2
            count = 1
            Ym = f(Xm)

            Error = tol + 1
            while
                if Yi*Ym < 0 then
                    X s= Xm
                    Ys = Ym
                else
                    X i= Xm
                    Yi = Ym
                    Fin if
                    Xaux = Xm
                    Xm = (Xi + Xs)/2
                    Ym = f(Xm)

                    Error = Abs(Xm - Xaux)
                    count = count + 1
                end if
            end while
            if Ym = 0 then
                print ‘Xm is a root’
            else if Error < tol then
                print ‘Xm It is an approximation to a root with a tolerance ‘tol’’
            else
                print ‘error in ‘Iter’’
            end if
        else
            print ‘The interval is inappropriate’
        end if
    end if
end if
``` 
        
### False rule.
It works the same as the bisection method, changing Only the method to select xm. In this case it is taken
a straight line from f (a) to f (b) and is taken as xm the value
where the x  intersects.

```bash
in f(), p0, p1, tol, iter
i = 1
while i <iter 
    p = p1-f(p1)*(p1-p0)/(f(p1)-f(p0))
    if |f(p)| < tol then
        print p
    end if
    i = i + 1
    if f(p).f(p1) < 0 then
        p0 = p1
        p1 = p
    else
        p1 = p
    end if
end while
if |f(p)| >= tol then
    print "the method finish in 'iter'"
end if
``` 
        
### Fixed point.
The method is based on the idea of ​​converting f (x) = 0, into x = g (x)
somehow.

The fundamental idea of ​​the method is to arrive at a point where
satisfies the equality x = g (x) or we are close enough to
do it

```bash
in f(x) g(x) x0 e N
out x1
count = 1
while abs f(x1) > e 
    x1 = g(x0)
    step = step + 1
    if step > N
        Print "Not Convergent"
    end if
    x0 = x1
end While

print x1
``` 
        
### Newton.
Let f ∈C 2 [a, b] and xv∈ [a, b] such that f (xv) = 0 and f ′ (xv) 6 = 0
then there exists d> 0 such that Newton's method generates a
sequence {xn} ∞n = 0 that converges to xv for any approximation
initial x0 ∈ [xv − d, xv + d].

```bash
in x0 f() fp() tol iter
while i == iter
    y = f(x0)
    yp= fp(x0)

    x1 = x0 - y/yp
    if abs(x1 - x0) <= tol 
        solutionFound = true
    end if

    x0 = x1                   
end while

if solutionFound
    println("Solution: ", x1)
else
    println("Did not converge")
end if
            
``` 
        
### Secante.
In the secant method we take two values ​​of the function for
create the secant line to it and obtain a new value. The
The logic behind this method is that it allows an approximation to the
Newton's method without the need to perform the derivative.

```bash
in x1, x0, tol, Iter
y0 = f(x0)
if y0 = 0 then
    print ‘x0 is root’
else
    y1 = f(x1)
    cont = 0
    Error = tol + 1

    while

        X2 = x1 – ((y1*(x1 x0))/Den)
        Error = Abs((X2 – x1)/ X2)
        x0 = x1
        y0 = y1
        x1 = X2
        y1 = f(x1)
        cont = cont + 1

    end while
    if y1 = 0 then
        print ‘x1 ir root’
    else if Error < tol then
        print ‘‘x1’ is an approximate root with a ‘tol’’
    else if Den = 0 then
        print ‘possibly a root’
    else
        print ‘failed in ‘Iter’ iter’
    end if
end if 
``` 
        
### Multiple roots.
Let f ∈C m [a, b]. The function has a multiplicity root m in xv if and only if:

0 = f (xv) = f ′ (xv) = f ′ ′ (xv) = ... = f (m − 1) (xv)

But f (m) (xv) is different from zero.

```bash
in x0, tol, Iter
y0 = f(x0)
d0 = fp(x0)
d20 = fpp(x0)
Deno = d0 ^ 2 - (y0 * d20)
count = 0
Error = tol + 1
while y0 != 0 & Deno != 0 & Error > tol & count < Iter
    x1 = x0 - (y0*d0) / Deno)
    y0 = f(X1)
    d0 = fp(X1)
    d20 = fpp(X1)
    Error = abs (X1 - x0)/X1)
    Deno= d0 ^ 2 - (y0 * d20)
    x0 = X1
    count = count + 1
end while
if y0 = 0 then
    print ‘x0 is a root’
else if Error < tol then
    print ‘‘x0’ is an approximate root with ‘tol’’
else if Deno = 0 then
    print ‘The denominator becomes zero’
else
    print ‘failed in ‘Iter’ iterations’
end if
``` 
        
## Solution of systems of linear equations.

### Gauss simple.
the general idea of ​​the method is to start from Ax = b to arrive at Ux = B where U is an upper triangular matrix.

```bash
int A, b
(n,m)= length(A)
a = augmentedMatrix (A,b)
if n = m then
    for k=1 until n-1
        for i=k+1 until n
            mik = aik / akk
            for j=k until n+1
                aij = aij - mikakj

            end for
        end for
    end for
    for i=n until 1
        sum = 0
        for p=i+1 until n
            sum = sum + aipxp
        end for
        xi = ( bi – sum ) / aii
    end for
else
    print ‘La matriz no es Cuadrada’
end if
print a
print x
``` 
        
### Gauss partial pivot.
In each stage k it is sought that akk (or the pivot) is of greater possible magnitude (absolute value) compared to others
values ​​in column k that are below akk.

```bash
in A, b
(n,m)= length(A)
a = augmentedMatrix (A,b)
if n = m then
    for k=1 until n-1
        higher = 0
        filam = k
        for p=k until n
            if higher < then
                higher =
                filam = p
            end if
        end for
        if higher = 0 then
            print ‘Suspended the process, Inenditas solutions’
        else
            if filam k then
                for j=1 until n+1
                    Aux = a(k, j)
                    a(k, j) = a(filam, j)
                    a(filam ,j) = Aux
                end for
            end if
        end if
        for i=k+1 until n
            mik = aik / akk
            for j=k until n+1
                aij = aij - mikakj
            end for
        end for
    end for
    for i=n until 1
        sum = 0
        for p=i+1 until n
            sum = sum + aipxp
        end for
        xi = ( bi – sum ) / aii
    end for
else
    print ‘La matriz no es Cuadrada’
end if
print a
print x
```   

### Gauss total pivot.
In each stage k it is sought that akk (or the pivot) is of greater possible magnitude (absolute value) compared to others
elements that are not part of the rows from F1 to Fk −1 or of the columns from C1 to Ck −1.

```bash
in A, b
(n,m)= length(A)
a = augmentedMatrix (A,b)
if n = m then
    for i=1 until n
        mark(i)= i
    end for
    for k=1 until n-1
        higher = 0
        filam = k
        columnam = k
        for p=k until n
            for r=k until n
                if higher < then
                    higher =
                    filam = p
                    columnam = r
                end if
            end for
        end for
        if higher = 0 then
            print: ‘Suspended the process, Inenditas solutions’
        else
            if filam k then
                for j=1 until n+1
                    Aux = a(k, j)
                    a(k, j) = a(filam, j)
                    a(filam ,j) = Aux
                end for
            end if
            if columnam k then
                for i=1 until n
                    Aux = a(i, k)
                    a(i, k) = a(i, columnam)
                    a(i, columnam) = Aux
                end for
                Aux = mark (k)
                mark (k) = mark (columnam)
                mark (columnam) = Aux
            end if
        end if
        for i=k+1 until n
            mik = aik / akk
            for j=k until n+1
                aij = aij - mikakj
            end for
        end for
    end for

    for i=n until 1
        sum = 0
        for p=i+1 until n
            sum = sum + aipxp
        end for
        xi = ( bi – sum ) / aii
    end for
    for i=n until 1
        for j=1 until n
            if mark(j) = i then
                k = j
            end if
        end for
        Aux = x(k)
        x(k) = x(i)
        x(i) = Aux
        Aux = mark(k)
        mark(k) = mark(i)
        mark(i) = Aux
    end for
else
    print: ‘La matriz no es Cuadrada’
end if
print a
print x
``` 
        

### Jacobi.

```bash
in A, b, x, iter, tol
cond = ||A|| * || A^-1 ||
print cond
det(A)
if det(A)=0 then
    print ‘ The determinant is zero, the problem has no solution only‘
end if
n = length(b)
d = diagonal(diagonal(A))
l = d – lowerTriangular(A)
u = d – upperTriangle(A)
T = (d ^ -1) * (l + u)
print T
SpectralRadius= max|val(T)|
if SpectralRadius > 1 then
    print ‘ Spectral radius greater than 1, method does not converge‘
end if
C= (d^-1 * b)
print C
i=0
error = tol + 1
while error>tol & i<iter
    xi = T*x + C
    i = i +1
    error =
    x=xi
end while
print table
``` 
        

### Gauss seidel.

```bash
in A, b, x, iter, tol
cond = ||A|| * || A^-1 ||
print cond
det(A)
if det(A)=0 then
    print ‘ The determinant is zero, the problem has no solution only‘
end if
n=lenght(b)
d=diagonal(diagonal(A))
l = d – lowerTriangular(A)
u = d – upperTriangle(A)
T = (d ^ -1) * (l + u)
print T
SpectralRadius= max|val(T)|
if SpectralRadius >1 then
    Muestre ‘ Spectral radius greater than 1, method does not converge‘
end if
C= (d^-1 * b)
print C
i=0
error = tol + 1
while error>tol & i<iter
    xi = T*x + C
    i = i +1
    error =
    x=xi
end while
print table
``` 
        

## Interpolation.

### Vandermonde.

    ```bash
        
    ``` 
        

### Divided differences.

    ```bash
        
    ``` 
        

### Lagrange.

```bash
in xi, yj
n= length(xi)
symbol(x)

for j=1 until n
    product = 1
    for i=1 until j-1
        product = product * ( x – x1j )
    Fin for
    product2 = 1
    for i=j+1 until n
        product2 = product2 * ( x – x1j )
    Fin for
    product3 = 1
    for i=1 until j-1
        product3 = product3 * ( x – x1j )
    Fin for
    product4 = 1
    for i=j+1 until n
        product4 = product4 * ( x – x1j )
    Fin for
    Lj = (product * product2)/(product3 * product4)
Fin for
Pn=0
for j=1 until n
    Pn = Pn + ( Lj * yij )
Fin for
print Pn
``` 


