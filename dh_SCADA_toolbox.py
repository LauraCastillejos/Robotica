import sympy as sp
from sympy.matrices import rot_axis3
# Para el ejemplo donde generamos la matriz DH
from spatialmath import *
from spatialmath.base import *
# Para poder Graficar
import matplotlib.pyplot as plt
import numpy as np
# Para usar el DH
import roboticstoolbox as rtb

scara = rtb.DHRobot(
    [
        rtb.RevoluteDH(d=0.160, a=0.350, alpha=0, qlim=[-2.58, 2.58]),
        rtb.RevoluteDH(d=0, a=0.300, alpha=0, qlim=[-2.61, 2.61]),
        rtb.PrismaticDH(theta=0, a=0, alpha=np.pi, offset=0.21, qlim=[-0.370, 0.0]),
        rtb.RevoluteDH(d=0, a=0, alpha=0, qlim=[-6.28, 6.28])
    ],
    name="SR6iA",base=SE3(0, 0, 0))
print(scara)

# Para modificar los angulos comodamente
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = -0.210  # Valor prismatico offset +0.210
joint4 = np.deg2rad(0)

T04DH = scara.fkine([joint1, joint2, joint3, joint4])  # Lo definimos asi por el offset
print(T04DH)

# Definir variables articulares
q = np.array([
    [0, 0, 0, 0],
    [joint1, 0, 0, 0],
    [joint1, joint2, 0, 0],
    [joint1, joint2, joint3, 0],
    [joint1, joint2, joint3, joint4],
    [joint1, joint2, joint3, 0],
    [joint1, joint2, 0, 0],
    [joint1, 0, 0, 0],
    [0, 0, 0, 0]
])

# Graficar con posiciones q, una cada 3 segundos
scara.plot(q=q, backend='pyplot', dt=3, limits=[-0.8, 0.8, -0.8, 0.8, -0.4, 0.6], shadow=True, jointaxes=True)

q1 = np.array([[0, 0, 0, 0]])
scara.teach(q1)