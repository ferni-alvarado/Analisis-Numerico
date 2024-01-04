from ej2 import inewton
import matplotlib.pyplot as plt

def fdex(x):
    return 1/x

x1 = [1, 2, 3, 4, 5]

y1 = []
for i in range(1,6):
    y1.append(fdex(i))

z = []
for j in range (1, 102):
    z.append(24/25 + j/25)

w = inewton(x1, y1, z)

y2 = [fdex(k) for k in z]

plt.plot(z, y2, label='funcion f')
plt.plot(z, w, label='polinomio p')
plt.ylabel("Eje y")
plt.xlabel("Eje x")
plt.show()
