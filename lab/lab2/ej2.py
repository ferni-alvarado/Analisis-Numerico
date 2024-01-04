
import math

def rbisec(fun, I, err, mit):
    u = I[0]
    v = I[1]
    hx = []
    hf = []
    if fun(u) * fun(v) >= 0:
        print("Tienen el mismo signo o alguna es igual a cero.")
        return hx, hf
    for k in range(mit):
        c = (u + v)/2
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if abs(fun(c))<err:
            break
        if fun(u)*fun(c) < 0:
            v = c
        else:
            u = c
    return(hx, hf) 

def fun_lab2ej2_a(x):
    return (math.tan(x)-2*x)

hx, hy = rbisec(fun_lab2ej2_a, [0.8, 1.4], 1e-5, 100)
print(hx, hy)

# la menor solucion positiva es 1.1655609130859372 #