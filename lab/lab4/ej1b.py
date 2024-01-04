import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat')

x = data[:,0]
y = data[:,1]
largo = len(x)

unos = np.ones(largo)
sum_x = np.dot(x,unos)
sum_x2 = np.dot(x,x)
sum_xy = np.dot(x,y)
sum_y = np.dot(y, unos)

a0 = ((sum_x2 * sum_y) - (sum_xy * sum_x)) / ((largo*sum_x2) - sum_x**2)
a1 = ((largo*sum_xy) - (sum_x * sum_y)) / ((largo*sum_x2) - sum_x**2)


plt.plot(x, y, '*')
plt.plot(x, a1 * x + a0)
plt.title("inciso b")
plt.show()