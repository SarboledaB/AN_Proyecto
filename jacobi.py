def entrada(mx,mr,n=100,c=0.0001):
    Jacobi(mx,mr,n,c)


def Jacobi(mx,mr,n,c):
    if len (mx) == len (mr): #Si mx y mr tienen la misma longitud, comience la iteración; de lo contrario, la ecuación no tiene solución
        x = [] # Valor inicial iterativo inicializado en una sola fila toda la matriz 0
        for i in range(len(mr)):
            x.append([0])
        count = 0 #count el número de iteraciones
        while count < n:
            nx = [] # Guardar el conjunto de valores después de una sola iteración
            for i in range(len(x)):
                nxi = mr[i][0]
                for j in range(len(mx[i])):
                    if j!=i:
                        nxi = nxi+(-mx[i][j])*x[j][0]
                nxi = nxi/mx[i][i]
                nx.append ([nxi]) # Calculado iterativamente el siguiente valor xi
                lc = [] # almacena el conjunto de errores entre los resultados de dos iteraciones
            for i in range(len(x)):
                lc.append(abs(x[i][0]-nx[i][0]))
            if max(lc) < c:
                return nx #Cuando el error cumple con los requisitos, devuelve el resultado del cálculo
            x = nx
            count = count + 1#Si el resultado de la iteración establecida aún no está satisfecho, la ecuación no tiene solución
    else:
        return False