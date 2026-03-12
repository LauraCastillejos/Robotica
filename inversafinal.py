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

L1 = 0.400 #Vamos a usar estos valores
L2 = 0.300
robot = rtb.DHRobot(
    [
        rtb.RevoluteDH(
            d=0.450, a=0.130, alpha=-np.pi/2,
            qlim=[np.deg2rad(-170), np.deg2rad(170)]
        ),
        rtb.RevoluteDH(
            d=0.000, a=0.600, alpha=0.0, offset=-np.pi/2,
            qlim=[np.deg2rad(-90), np.deg2rad(150)]
        ),
        rtb.RevoluteDH(
            d=0.000, a=0.150, alpha=-np.pi/2,
            qlim=[np.deg2rad(0), np.deg2rad(170)]
        ),
        rtb.RevoluteDH(
            d=0.760, a=0.000, alpha=np.pi/2,
            qlim=[np.deg2rad(-190), np.deg2rad(190)]
        ),
        rtb.RevoluteDH(
            d=0.000, a=0.000, alpha=-np.pi/2,
            qlim=[np.deg2rad(-120), np.deg2rad(120)]
        ),
        rtb.RevoluteDH(
            d=0.100, a=0.000, alpha=0.0,
            qlim=[np.deg2rad(-360), np.deg2rad(360)]
        ),
    ],
    name="Robot_6GDL_DH",
    base=SE3(0, 0, 0)
)

print("\n================ TABLA DH DEL ROBOT ================\n")
print(robot)

# ==========================================================
# 4. CONFIGURACIÓN ARTICULAR DE PRUEBA
# ==========================================================
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(0)
joint3 = np.deg2rad(90)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

q_home = [joint1, joint2, joint3, joint4, joint5, joint6]

T06_robot = robot.fkine(q_home)

print("\n================ FKINE CON ROBOTICSTOOLBOX ================\n")
print(T06_robot)
#print(robot)
#tool=SE3()#Pose de efector final

#Validamos con la directa el DH
#Para modificar los angulos comodamente
joint1 = 30#En grados
joint2 = 30

T=robot.fkine([np.deg2rad(joint1), np.deg2rad(joint2), np.deg2rad(joint3), np.deg2rad(joint4), np.deg2rad(joint5), np.deg2rad(joint6)], tool=None)
print(T)
Tn = np.array(T).astype(np.float64) #Convertimos a numpy 
robot.plot(q_home, limits=[-0.8, 0.8, -0.8, 0.8, -0.1, 0.2], backend='pyplot',shadow=True, jointaxes=True, block=True)

print(f"Los angulos en la Cdieracta son ({joint1:.2f}, {joint2:.2f})")
print(f"La coordenada es ({Tn[0, 3]:.3f},{Tn[1, 3]:.3f}), que pasamos a la inversa...")

t = T.t #extrayendo ela marte de la matriz t
# print(t)
q = SE3([round(t[0], 4), round(t[1], 4), 0]) #tipo de dato extrae x, y y redondea a 4 decimales, extraemos la coordenada q
# print(q)

#Cinematica Inversa
we = [1, 1, 1, 0, 0, 0]
sol = robot.ikine_LM(Tep=q, q0=[0,0], ilimit=5000, slimit=1000, tol=0.000005, joint_limits=True, mask=we)
print(sol)

# Mostrar resultado
if sol.success:
    # Extraemos los ángulos del resultado
    theta1=np.rad2deg(sol.q[0]) # Convertimos a grados
    theta2=np.rad2deg(sol.q[1]) # Convertimos a grados  
    print


#inverse kinematics
#para hacer la kinematica inversa, se aproxima 
#se le ponen puros 1 por que es un robot plano
#q0=[0,0] # quiere decir que esta en la posicion 0 si tenemos el robot en otra posicion, [] aqui tenemos que poner la posicion
#ilimit y slimit son limites de interaccion
#revisar si success es verdadero
