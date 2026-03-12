import numpy as np
import matplotlib.pyplot as plt
from spatialmath import *
from spatialmath.base import *
from math import pi

# np.set_printoptions(
#     formatter={'float': lambda x: f"{0:8.4g}" if abs(x) < 1e-10 else f"{x:8.4g}"})

# Rx = rotx(90, unit="deg")
# print(Rx)
# print('\n')

# Ry = roty(90, unit="deg")
# print(Ry)
# print('\n')

# Rz = rotz(90, unit="deg")
# print(Rz)
# print('\n')

# trplot(Ry)
# tranimate(Ry)
# plt.show()

#Referencias T0
T0 = rotz(0, unit="deg")
trplot(T0, dims=[-1, 1, -1, 1, -1,1], color='k') #Dibujar


#Sistema de coordenadas rotando(TA)
TA = rotz(90, unit="deg")
trplot(TA, dims=[-1, 1, -1, 1, -1,1], color='k') #Dibujar

#Definir el pinto P con respecto a T0
P = np.array([1, 0, 0])
ax = plt.gca()
ax.plot(P[0], P[1], P[2], color='r', label='P')

#configurar plot
plt.gca().view_init(elev=25, azim=44) #Perspectiva

#Mostrar la trama
plt.show()

print("P en T0: ", P)
Pos_TA = P @ TA
print("Posmult. de P respecto a TA: ", Pos_TA)  





