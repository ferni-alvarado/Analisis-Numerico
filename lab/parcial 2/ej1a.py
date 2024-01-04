import numpy as np
import matplotlib.pyplot as plt

#datos del archivo y su grafico 

data = np.loadtxt('.\irma.csv', delimiter=',')
long = data[:,1]
lat = data[:,2]


fig, ax = plt.subplots()
fig.suptitle('datos')
ax.plot(long,lat, 'o')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
plt.show()