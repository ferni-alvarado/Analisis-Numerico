
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
