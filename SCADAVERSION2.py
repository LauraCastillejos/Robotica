import roboticstoolbox as rTBA
import numpy as np
import matplotlib.pyplot as plt

from spatialmath import *
from spatialmath.base import *

from sympy import Symbol, Matrix

theta = Symbol('theta')
R = Matrix(rot2(theta))
print("R:")
print(R)

#Convertir grados a radianes
theta_deg = 30
theta_rad = np.deg2rad(theta_deg)

# T0 = transl2(0,0) #Referencia
# trplot2(T0, frame="Ref", color='k')

# TA = trot2(30,"deg")
# print(TA)
# trplot2(TA, frame='A', color='b') 

# plot_circle(4,(0,0),'b--')

# TBA = TA @ transl2(4,0) @ trot2(0, "deg")
# print(TBA)
# trplot2(TBA, frame='B', color='g') 

# origin_TBA = TBA [:2,2]
# plot_circle(3,(origin_TBA[0],origin_TBA[1]),'g--')

# TCBA = TBA @ transl2(3,0)
# print(TCBA)
# trplot2(TCBA, frame='C', color='y') 

# origin_TCBA = TCBA [:2,2]
# plot_circle(3,(origin_TBA[0],origin_TBA[1]),'g--')

# P = np.array((origin_TCBA[0],origin_TCBA[1]))
# plot_point(P,"ko", text="P")
# print("Coords T0: {:.4f}, {:.4f}".format(P[0],P[1]))

# P1 = homtrans(np.linalg.inv(TA),P)
# print("P1")
# print(P1)

# P_TA = homtrans(np.linalg.inv(TA),P)
# print("Coords T0: {:.4f}, {:.4f}".format(P_TA[0,0],P_TA[1,0]))

# P_TBA = homtrans(np.linalg.inv(TBA),P)
# print("Coords T0: {:.4f}, {:.4f}".format(P_TBA[0,0],P_TBA[1,0]))

# plt.axis('equal')
# plt.grid(True)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('SCARA 2D')
# plt.show() # Mostrar ventana


np.set_printoptions(
    formatter={'float': lambda x : "{0:8.4g}" if abs(x) < 1e-4 else "{0:8.4f}"})

from sympy import *
from sympy import Symbol, Matrix, simplify  
from sympy.matrices import rot_axis3

theta1, L1, theta2, L2 = symbols('theta1 L1 theta2 L2') 

#theta1 = Symbol('theta1')
#L1 = Symbol('L1')
#theta2 = Symbol('theta2')
#L2 = Symbol('L2')

T01 = trotz(theta1) @ transl(L1, 0, 0)
print(f"Primera transformación T01:\n{T01}\n")

T12 = trotz(theta2) @ transl(L2, 0, 0)
print(f"Segunda transformación T12:\n{T12}\n")

T02 = simplify(T01 @ T12) #Transformacion completa
print(f"Transformación completa T02:\n{T02}\n") 

#Convertir el ndarrayy a una matriz de sympy
M = Matrix(T02)
#Simplificar la matriz
M_simplified = M.applyfunc(simplify)

#Mejor visualizacion
def nice_print(matrix):
    return "\n".join(["".join([str(entry.evalf()) for entry in row]) for row in matrix.tolist()])

#Imprimir la matriz simplificada
print(nice_print(M_simplified))
print('\n')

#Sustituir y resolver operaciones
M_evaluated = M_simplified.subs({theta1: np.deg2rad(30), L1: 4, theta2: np.deg2rad(0), L2: 3}).evalf()  
print(nice_print(M_evaluated))

