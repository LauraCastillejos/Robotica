import sympy as sp
import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3
import matplotlib.pyplot as plt

# =============================
# 1 Definir matriz DH
# =============================

theta, d, a, alpha = sp.symbols('theta d a alpha')

T = sp.Matrix([
[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
[sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
[0, sp.sin(alpha), sp.cos(alpha), d],
[0,0,0,1]
])

print("Matriz DH general")
sp.pprint(T)


# =============================
# 2 Variables articulares
# =============================

theta_1,theta_2,theta_3,theta_4,theta_5,theta_6 = sp.symbols(
'theta_1 theta_2 theta_3 theta_4 theta_5 theta_6')


# =============================
# 3 Matrices DH individuales
# =============================

T01 = T.subs({theta:theta_1, d:0.495, a:0.175, alpha:-sp.pi/2})
T12 = T.subs({theta:theta_2-sp.pi/2, d:0, a:1.095, alpha:0})
T23 = T.subs({theta:theta_3, d:0, a:0.175, alpha:-sp.pi/2})
T34 = T.subs({theta:theta_4, d:1.2305, a:0, alpha:sp.pi/2})
T45 = T.subs({theta:theta_5, d:0, a:0, alpha:-sp.pi/2})
T56 = T.subs({theta:theta_6, d:0.085, a:0, alpha:0})

print("\nT01")
sp.pprint(T01)

print("\nT12")
sp.pprint(T12)

print("\nT23")
sp.pprint(T23)

print("\nT34")
sp.pprint(T34)

print("\nT45")
sp.pprint(T45)

print("\nT56")
sp.pprint(T56)


# =============================
# 4 Cinemática directa
# =============================

T06 = T01*T12*T23*T34*T45*T56

print("\nMatriz T06 simbólica")
sp.pprint(T06)


# =============================
# 5 Evaluar en posición HOME
# =============================

q1=np.deg2rad(0)
q2=np.deg2rad(-90)
q3=np.deg2rad(0)
q4=np.deg2rad(0)
q5=np.deg2rad(0)
q6=np.deg2rad(0)

T06_eval=T06.subs({
theta_1:q1,
theta_2:q2,
theta_3:q3,
theta_4:q4,
theta_5:q5,
theta_6:q6
})

print("\nT06 evaluada")
sp.pprint(T06_eval)


# =============================
# 6 ROBOTICS TOOLBOX
# =============================

robot=rtb.DHRobot([

rtb.RevoluteDH(d=0.495,a=0.175,alpha=-np.pi/2),

rtb.RevoluteDH(d=0,a=1.095,alpha=0,offset=-np.pi/2),

rtb.RevoluteDH(d=0,a=0.175,alpha=-np.pi/2),

rtb.RevoluteDH(d=1.2305,a=0,alpha=np.pi/2),

rtb.RevoluteDH(d=0,a=0,alpha=-np.pi/2),

rtb.RevoluteDH(d=0.085,a=0,alpha=0)

],name="ABB IRB 4600-45/2.05",base=SE3(0,0,0))

print("\nRobot declarado")
print(robot)


# =============================
# 7 Cinemática con toolbox
# =============================

q=np.deg2rad([0,-90,0,0,0,0])

T=robot.fkine(q)

print("\nMatriz FK con toolbox")
print(T)


# =============================
# 8 Gráfica del robot
# =============================

robot.plot(q)