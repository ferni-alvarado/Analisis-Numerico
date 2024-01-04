import numpy as np
import matplotlib.pyplot as plt

data_1 = np.loadtxt('https://raw.githubusercontent.com/lbiedma/anfamaf2022/main/datos/datos3a.dat')

# y = C * x ** A --> ln(y) = ln(C * x ** A)
#                    ln(y) = ln(C) + A * ln(x)
x = data_1[0]
y = data_1[1]
print(x)
y_p = np.log(y)
x_p = np.log(x)
coeficientes = np.polyfit(x_p,y_p,1)
print(coeficientes)

a = coeficientes[0]
c = np.exp(coeficientes[1])

plt.plot(x,y, 'o')
plt.plot(x, c * x ** a)
plt.show()