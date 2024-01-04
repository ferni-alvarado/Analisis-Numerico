def f(x):
    y = (((x**2) + 1)**(0.5)) - 1
    return y
def g(x):  
    g = (x**2)/((((x**2) + 1)**(0.5)) + 1)
    return g

for i in range(20):
    x = 8**(-i)
    print(f"f(x) = {f(x)}, g(x) = {g(x)}")

  
''' para las primeras 8 i las dos funciones dan igual, despues del 8 f da 0 y g cada vez
es mas pequeño'''
'''g es mas confiable'''
