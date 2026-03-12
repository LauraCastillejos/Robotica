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

L1 = 0.400
L2 = 0.300
robot = rtb.DHRobot( 
    [
        rtb.RevoluteDH(d=0, a=L1, alpha=0, qlim=[-2.61, 2.61]),
        rtb.RevoluteDH(d=0, a=L2, alpha=0, qlim=[-2.61, 2.61])
    ],
    name="2Links", base=SE3(0, 0, 0))
print(robot)   

# q1=np.array([[0, 0]])
# robot.teach(q1)

#Validamos con la directa el DH
#Para modificar los angulos comodamente
joint1 = 30#En grados
joint2 = 30

T=robot.fkine([np.deg2rad(joint1), np.deg2rad(joint2)])
print(T)
Tn = np.array(T).astype(np.float64) #Convertimos a numpy 

print(f"Los angulos en la Cdieracta son ({joint1:.2f}, {joint2:.2f})")
print(f"La coordenada es ({Tn[0, 3]:.3f},{Tn[1, 3]:.3f}), que pasamos a la inversa...")

#Las ecuaciones que calculamos de forma geometrica
r1 = np.sqrt((x**2)+(y**2))


