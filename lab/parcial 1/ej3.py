import math

def serie_seno(x): 
    y = 0
    for k in range(5):
        y = y + (((-1)**k / math.factorial(2*k+1))*x**(2*k+1))
    return y

#crea la funcion del metodo de biseccion

def rbisec(fun, I, mit, err):
    hx = []
    hf = []
    a = I[0]
    b = I[1]

    u = fun(a)
    v = fun(b)
    if u * v > 0:
        print("las dos funciones tienen el mismo signo, no hay raiz")
        return None

    for k in range(mit):
        c = a + ((b - a) / 2)
        w = fun(c)
    
        hx.append(c)
        hf.append(w)
        
        if abs(w) < err:
            print("se satisface la tolerancia con valor {} en {}".format((abs(w)), c))
            break
        if w * v < 0:
            a = c
            u = w
        else:
            b = c
            v = w

    return hx, hf


'''para su aplicacion se crean 2 listas aplicando 
metodo de biseccion con los parametros dados y se muestran sus ultimos valores'''

l1, l2 = rbisec(serie_seno, [2, 4], 100, 1e-5)
l3, l4 = rbisec(serie_seno, [4, 5], 100, 1e-5)

print("las raices son: {} y {}".format(l1[-1], l3[-1]))

#las 2 raices positivas son: 3.148681640625 y 4.9631500244140625