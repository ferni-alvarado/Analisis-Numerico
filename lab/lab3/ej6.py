import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from ej2 import inewton
from ej1 import ilagrange



x = [-3,-2,-1,0,1,2,3]
y = [1,2,5,10,5,2,1]
z = np.linspace(0,7,7)

p1 = inewton(x,y,z)
p2 = ilagrange(x,y,z)
f = interpolate.interp1d(x,y, kind='linear')
p3 = f(z)

plt.plot(x, p1, label='p1')
plt.plot(x, p2, label='p2')
plt.plot(x, p3, label='p3')
plt.show()
