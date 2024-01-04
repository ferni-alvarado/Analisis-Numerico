def ilagrange(x, y, z):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud")
        return None

    n = len(x)
    w = []
    for zi in z:
        # sumatoria de los polinomios base l_i por y_i
        wi = 0.0
        for i in range(n):
            # productoria para generar el polinomio base l_i evaluado en z_i
            li = 1.0
            for j in range(n):
                if j != i:
                    li = li * (zi - x[j]) / (x[i] - x[j])

            wi = wi + y[i] * li
        w.append(wi)
    return w

