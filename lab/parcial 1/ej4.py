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

