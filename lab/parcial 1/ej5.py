import math

def serie_seno(x): 
    y = 0
    for k in range(5):
        y = y + (((-1)**k / math.factorial(2*k+1))*x**(2*k+1))
    return y

def rsteffensen(fun, x0, err, mit):
    l = fun(x0)                 #crea la funcion en el valor x0
    hf = []                     #crea las listas vacias 
    hx = []
    for k in range(mit):        #realiza la aplicacion del metodo
        s = x0 + l
        v = fun(s) - fun(x0)  
        if v != 0:
            x1 = x0 - ((l**2)/v)
            hx.append(x1)
            hf.append(l)
            l = fun(x1)   
        if (abs (l) < err):
            break                      
        x0 = x1
    return hx, hf

#crea 3 listas aplicando metodo de steffensen en esos parametros

l1, l2 = rsteffensen(serie_seno, 3, 1e-5, 100)
l3, l4 = rsteffensen(serie_seno, 6, 1e-5, 100)

l5, l6 = rsteffensen(serie_seno, 4.5, 1e-5, 100)

#se muestran la cantidad de elementos de las listas 
# que representan la cantidad de iteraciones
print("las raices son:", l1[-1], l3[-1], l5[-1])
print("las iteraciones con x0 = 3 son: {}, x0 = 6: {}, x0= 4.5: {}".format(len(l1), len(l3), len(l5)))

#las iteraciones con x0 = 3 son: 1, x0 = 6: 69, x0= 4.5: 100
# al iniciar la busqueda con 4.5 alcanza la maxima cantidad de iteraciones y llega a un numero negativo.