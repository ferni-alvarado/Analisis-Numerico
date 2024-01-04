import matplotlib.pyplot as plt
import math


def serie_seno(x): 
    y = 0
    for k in range(5):
        y = y + (((-1)**k / math.factorial(2*k+1))*x**(2*k+1))
    return y

'''crea las 2 listas que representan los puntos (x, f(x)) 
y procede a graficar la funcion'''

x = [0.01 * i for i in range(0, 650)]
y = [serie_seno(0.01 * i) for i in range(0, 650)]

plt.plot(x, y, '-')
plt.ylabel("Eje y")
plt.xlabel("Eje x")
plt.title("Primeros 5 terminos de la serie de Taylor del seno alrededor de cero")
plt.show()

