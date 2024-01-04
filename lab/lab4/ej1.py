import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos1a.dat')

x = data[:,0]
y = data[:,1]
sum_x = 0
sum_x_2 = 0
sum_xy = 0
sum_y = 0
sum_y_2 = 0
for i in range(0, 12):
    sum_x += x[i]
    sum_x_2 += x[i]**2
    sum_xy += x[i]*y[i]
    sum_y += y[i]

print(len(x))

a0 = ((sum_x_2 * sum_y) - (sum_xy * sum_x)) / ((12*sum_x_2) - sum_x**2)
a1 = ((12*sum_xy) - (sum_x * sum_y)) / ((12*sum_x_2) - sum_x**2)

def f(x):
    return a1*x + a0

z = np.linspace(0,11,30)
y2 = []
for i in z:
    y2.append(f(i))
print(len(y2))

plt.plot(x,y,'o',label='data')
plt.plot(z,y2,label='aproximacion')

plt.legend()
plt.show() 

