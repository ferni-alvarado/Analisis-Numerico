
def busqueda_raiz(a):
    fun = lambda x: (x**3 - a, 3*x**2)
    return fun(2)
"""es lo mismo que:
    def fun(x):
        return x ** 3 - a, 3 * x ** 2
        nada mas que adentro de la funcion busqueda raiz
    """

from ej3 import rnewton

def buscar_raiz3(a):
    fun = lambda x: (x ** 3 - a, 3 * x ** 2)

    return fun(a)

hx, hf = rnewton(buscar_raiz3, 27, 100, 1e-6)
print(hx[-1])

