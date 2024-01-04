import math

#crea la funcion de los primeros 5 terminos de la Serie de Taylor del seno

def serie_seno(x): 
    y = 0
    for k in range(5):
        y = y + (((-1)**k / math.factorial(2*k+1))*x**(2*k+1))
    return y

aplicacion = serie_seno(2)
print (aplicacion)

def serie_seno2(x):
    a = []
    for k in range(5):
        a.append(((-1)**k / math.factorial(2*k+1))*x**(2*k+1))
    return a

aplicacionlista = serie_seno2(2)
print(aplicacionlista)

''' en el segundo caso se muestra termino por termino de la sumatoria'''
