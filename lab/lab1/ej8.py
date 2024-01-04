def mala(a,b,c):
    x_1 = ((-b) - (((b**2) - 4*a*c)**0.5))/2*a
    x_2 = ((-b) + (((b**2) - 4*a*c)**0.5))/2*a
    return (x_1, x_2)

[x_1, x_2] = mala(1, 4, -5)
print(x_1, x_2)

def buena(a,b,c):
    if b >= 0:
        x_1 = ((-b) - (((b**2) - 4*a*c)**0.5))/2*a
    elif b < 0:
        x_1 = ((-b) + (((b**2) - 4*a*c)**0.5))/2*a
    x_2 = -b/a - x_1
    return x_1, x_2

[x_1, x_2] = buena(1, 4, -5)
print(x_1, x_2)

