# import roboticstoolbox as rtb
# import numpy as np
# import matplotlib.pyplot as plt

# from spatialmath import *
# from spatialmath.base import *

# from sympy import Symbol, Matrix

# # theta = Symbol('theta')
# # R = Matrix(rot2(theta)) 
# # print(R)

# #Convertir grados a radianes
# theta_deg = 30
# theta_rad = np.deg2rad(theta_deg)

# R = rot2(theta_rad)
# print(R)

# T0 = transl2(0,0) #Referencia
# #trplot2(T0, frame='0', color='k') # Dibujamos en plot

# # Traslacion de 2,2 seguida de una rotacion de 30 grados
# # TA = transl2(1,2) 
# # print(TA)
# # trplot2(TA, frame='A', color='b') 

# # Traslacion de 2,2 seguida de una rotacion de 30 grados
# TA = transl2(1,2) @ trot2(30,"deg")
# print(TA)
# trplot2(TA, frame='A', color='b') 

# P = np.array([4,3]) # Punto en coordenadas homogeneas 
# plot_point(P, "ko", text="P") # Dibujamos el punto en el plot 

# # Rotacion de 30 grados de translacion 1,2
# # TB = trot2(30, "deg") @ transl2(1,2)
# # print(TB)
# # trplot2(TB, frame='B', color='r') 


# trplot2(R) # Dibujamos en plot 
# plt.axis('equal')
# plt.grid(True)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Rotación 2D')
# plt.show() # Mostrar ventana

# # R = rot2(theta_rad)
# # print(R) 

# # R2 = trot2(theta_rad)
# # print(R2)   

import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

# theta = Symbol('theta')
# R = Matrix(rot2(theta)) 
# print(R)

#Convertir grados a radianes
theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

R = rot2(theta_rad)
print(R)

T0 = transl2(0,0) #Referencia
trplot2(T0, frame="Ref", color='k')

# Traslacion A
TA = transl2(1,2) @ trot2(30,"deg")
print(TA)
trplot2(TA, frame='A', color='b') 

# Rotacion B
'''
TB = trot2(30, "deg") @ transl2(1,2)
print(TB)
trplot2(TB, frame='B', color='r') 
'''

P = np.array([4,3])
plot_point(P,"ko", text="P")
print(P)

P1 = homtrans(np.linalg.inv(TA), P) 
print(P1)      

plt.axis('equal')
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cartesian')
plt.show() # Mostrar ventana