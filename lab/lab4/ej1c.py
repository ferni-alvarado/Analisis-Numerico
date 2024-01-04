import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return ((3/4)*x - (1/2))

x = np.linspace(0,10,20)
y = []
for i in x:
    y.append(f(i))

# Aplicamos una desviación a cada punto en y por una distribución normal
dispersion = np.random.randn(20)
puntos_con_ruido = y + dispersion

# Hacemos un ajuste lineal sobre esta nueva nube de puntos
ajuste = np.polyfit(x, puntos_con_ruido, 1)
# Evaluamos en x este ajuste para graficar
recta_ajustada = np.polyval(ajuste, x)

plt.plot(x, y, '*')
plt.plot(x, puntos_con_ruido, 'o')
plt.plot(x, recta_ajustada)
plt.show()
