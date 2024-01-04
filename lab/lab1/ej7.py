def potencia_enesima(n,x):
    m = x**n
    return m

x = int(input("ingrese un numero: "))
for y in range(1,6):
    print("{} elevado a {} es:".format(x, y), potencia_enesima(y, x))





