# User Manual

## First view
in this first window we will find the different categories of the methods:
    - Numerical solution of nonlinear equations.
    - Solution of systems of linear equations.
    - interpolation.

## Numerical solution of nonlinear equations.
In this window we find the -----------------------------

### Incremental searches.

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
        
- **How use**

### Bisection.

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
        
- **How use**

### False rule.

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
        
- **How use**

### Fixed point.

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
        
- **How use**

### Newton.

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
        
- **How use**

### Secante.

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
        
- **How use**

### Multiple roots.

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
        
- **How use**

## Solution of systems of linear equations.
In this window we find the -----------------------------

### Gauss.

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
        
- **How use**

### Gauss.

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
        
- **How use**

### Gauss.

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
        
- **How use**

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
        
- **How use**

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
        
- **How use**

## Interpolation.
In this window we find the -----------------------------

### Vandarmonde.

    ```bash
        
    ``` 
        
- **How use**

### Divided differences.

    ```bash
        
    ``` 
        
- **How use**

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


