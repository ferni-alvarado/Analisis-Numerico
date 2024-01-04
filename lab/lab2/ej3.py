def rnewton(fun, x0, mit, err):
    l = fun(x0)
    v = l[0]
    hf = []
    hx = []
    for k in range(mit):
        if l[1] != 0:
            x1 = x0 - (v/l[1])
            l = fun(x1)
            v = l[0]
            hx.append(x1)
            hf.append(l)
        if ((abs (x1) - abs(x0)) / abs(x0) < err) or (abs (v) < err):
            break
        x0 = x1
    return hf, hx


        



