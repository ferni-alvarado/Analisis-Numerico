import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#ejercicio a

x = [0, 1.5, 2, 2.9, 4, 5.6, 6, 7.1, 8.05, 9.2, 10, 11.3, 12]
y = [0.1, 0.2, 1, 0.56, 1.5, 2.0, 2.3, 1.3, 0.8, 0.6, 0.4, 0.3, 0.2]


plt.plot(x,y,'o',label='datos discretos')
plt.legend()
plt.show()

#ejercicio b 

''' toma como parametros los valores de x e y '''

def trapecio_adaptativo(x, y):
    sum = 0
    for i in range(0, len(x)-1):
        sum = sum + (x[i+1] - x[i])/2 * (y[i] + y[i+1])     
    return sum

# ejercicio c

'''primero calculo el area con el metodo de integracion de trapecio adaptativo,
luego lo mulitplico por 10 para obtener la cantidad de tierra que quitar'''

quitar = 10* trapecio_adaptativo(x, y)

print("Metros cubicos a remover: ", quitar) 