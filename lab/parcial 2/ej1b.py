import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

data = np.loadtxt('.\irma.csv', delimiter=',')
hs = data[:,0]
long = data[:,1]
lat = data[:,2]

def ilagrange(x, y, z):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud")
        return None
    n = len(x)
    w = []
    for zi in z:
        # sumatoria de los polinomios base l_i por y_i
        wi = 0.0
        for i in range(n):
            # productoria para generar el polinomio base l_i evaluado en z_i
            li = 1.0
            for j in range(n):
                if j != i:
                    li = li * (zi - x[j]) / (x[i] - x[j])

            wi = wi + y[i] * li
        w.append(wi)
    return w

#busco las horas que faltan datos
horas_inter = np.array([i for i in range(1, 24) if i not in hs])

#realizo la interpolacion de Lagrange
w = ilagrange(hs, long, horas_inter)

#efectuo el metodo de Spline cubico
s = interpolate.interp1d(hs,long, kind="cubic")


fig, ax = plt.subplots()
fig.suptitle('longitud')
ax.plot(hs, long, 'o', label='longitud por hora', color='green')
ax.plot(horas_inter, s(horas_inter),'o', label='interpolacion por Spline cubico')
ax.plot(horas_inter, w,'o', label='interpolacion de Lagrange', color = 'red')
ax.set_xlabel('hora')
ax.set_ylabel('longitud')
ax.legend()

#repito el proceso para los datos de latitud

w2 = ilagrange(hs, lat, horas_inter)
s2 = interpolate.interp1d(hs,lat, kind="cubic")

fig, ax = plt.subplots()
fig.suptitle('latitud')
ax.plot(hs, lat, '*', label='longitud por hora', color='purple')
ax.plot(horas_inter, s2(horas_inter),'o', label='interpolacion por Spline cubico')
ax.plot(horas_inter, w2,'^', label='interpolacion de Lagrange', color = 'orange')
ax.set_xlabel('hora')
ax.set_ylabel('latitud')
ax.legend()




plt.show()
