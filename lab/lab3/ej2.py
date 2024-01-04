from ssl import SSL_ERROR_WANT_X509_LOOKUP


def dif_divididas(x, y):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud")
        return None
    c = []
    n = len(x)
    for i in range(n):
        c.append([0]*(n-i))     #multiplico la lista de un elemento por la cantidad de elementos de la fila de la matriz
        c[i][0] = y[i]          #añado el primer elemento de cada sublista i -> f(xi)
    for j in range(1,n):
        for i in range(n-j):
            c[i][j] = (c[i+1][j-1] - c[i][j-1])/(x[i+j]-x[i])
    coefs = c[0]
    return coefs

 


def inewton(x, y, z):
    c = dif_divididas(x,y)
    n = len(x)
    w = []
    for zi in z:
        sum = c[0]        
        for i in range(1, n):
            p = 1.0
            for j in range(i-1):
                p = p * (zi-x[j])
            sum = sum + c[i]*p
        w.append(sum)
    return w
    