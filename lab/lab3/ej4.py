from ej2 import inewton
from math import cos, pi 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+25*(x**2))

z = np.linspace(-1,1, 200)
y = [f(i) for i in z]

fig = plt.figure()
ax = []
for idx in range(1,16):
    x1 = [((2*(i-1)/idx)-1) for i in range(1,idx+2)]
    y1 = [f(i) for i in x1]
    x2 = [(cos(((2*i+1)/(2*idx+2))*pi)) for i in range(0,idx+1)]
    y2 = [f(i) for i in x2]
    pn = inewton(x1, y1, z)
    qn = inewton(x2, y2, z)
    ax.append(fig.add_subplot(5,3,idx)) # fila, columna, idx
    ax[-1].plot(z, y)
    ax[-1].plot(z, pn)
    ax[-1].plot(z, qn)
    ax[-1].grid()

plt.show()

