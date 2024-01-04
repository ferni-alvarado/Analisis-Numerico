from ej1 import rbisec
from math import tan
import matplotlib.pyplot as plt

def fun_lab2ej2_a(x):
    return 2 * x - tan(x)

hx, hf = rbisec(
    fun_lab2ej2_a, [0.8, 1.4],
    1e-5, 100
)


x = [0.01 * i for i in range(80, 141)]
y = [fun_lab2ej2_a(0.01 * i) for i in range(80, 141)]
plt.plot(x, y)
plt.plot(hx, hf, '*')
plt.plot(hx[-1], hf[-1], 'ok')
plt.title("Puntos Visitados")
plt.show()