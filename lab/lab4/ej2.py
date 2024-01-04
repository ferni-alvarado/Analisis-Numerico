#usaR POLYFIT para generar el la aprox polinomial 
#recibe los datos y el grado que quiero, en este caso 5
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,49)
y = []
for i in x:
    y.append(np.arcsin(i))

ajuste = np.polyfit(x, y, 5)
recta_ajustada = np.polyval(ajuste, x)

plt.plot(x, y, '*')
plt.plot(x, recta_ajustada, 'o')
plt.show()
