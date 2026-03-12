import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

from spatialmath import *
from spatialmath.base import *
from spatialmath.base import trplot

# =========================
# 1. Definir símbolos
# =========================
theta, d, a, alpha = sp.symbols('theta d a alpha')

# Matriz DH simbólica
T = sp.Matrix([
    [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),  sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
    [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
    [0,              sp.sin(alpha),               sp.cos(alpha),               d],
    [0,              0,                           0,                           1]
])

print("Matriz DH general:")
sp.pprint(T)

# =========================
# 2. Variables articulares
# =========================
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols(
    'theta_1 theta_2 theta_3 theta_4 theta_5 theta_6'
)

# =========================
# 3. Parámetros DH de la tabla
#    (convertidos de mm a m)
# =========================
T01 = T.subs({
    d: 450/1000,
    a: 130/1000,
    alpha: -sp.pi/2,
    theta: theta_1
})

T12 = T.subs({
    d: 0,
    a: 600/1000,
    alpha: 0,
    theta: theta_2
})

T23 = T.subs({
    d: 0,
    a: 150/1000,
    alpha: -sp.pi/2,
    theta: theta_3
})

T34 = T.subs({
    d: 760/1000,
    a: 0,
    alpha: sp.pi/2,
    theta: theta_4
})

T45 = T.subs({
    d: 0,
    a: 0,
    alpha: -sp.pi/2,
    theta: theta_5
})

T56 = T.subs({
    d: 100/1000,
    a: 0,
    alpha: 0,
    theta: theta_6
})

print("\nT01:")
sp.pprint(T01)
print("\nT12:")
sp.pprint(T12)
print("\nT23:")
sp.pprint(T23)
print("\nT34:")
sp.pprint(T34)
print("\nT45:")
sp.pprint(T45)
print("\nT56:")
sp.pprint(T56)

# =========================
# 4. Cinemática directa total
# =========================
T06 = T01 @ T12 @ T23 @ T34 @ T45 @ T56
T06_s = T06.applyfunc(sp.simplify)

print("\nT06 simbólica simplificada:")
sp.pprint(T06_s)

# =========================
# 5. Sustituir valores de theta de la tabla
# =========================
joint1 = np.deg2rad(0)
joint2 = np.deg2rad(-90)
joint3 = np.deg2rad(0)
joint4 = np.deg2rad(0)
joint5 = np.deg2rad(0)
joint6 = np.deg2rad(0)

T06_solved = T06_s.subs({
    theta_1: joint1,
    theta_2: joint2,
    theta_3: joint3,
    theta_4: joint4,
    theta_5: joint5,
    theta_6: joint6
})

print("\nT06 evaluada:")
sp.pprint(sp.N(T06_solved, 4))

# =========================
# 6. Cálculo numérico de cada frame
# =========================
T0 = np.eye(4)

T01_n = np.array(T01.subs({theta_1: joint1})).astype(np.float64)
T12_n = np.array(T12.subs({theta_2: joint2})).astype(np.float64)
T23_n = np.array(T23.subs({theta_3: joint3})).astype(np.float64)
T34_n = np.array(T34.subs({theta_4: joint4})).astype(np.float64)
T45_n = np.array(T45.subs({theta_5: joint5})).astype(np.float64)
T56_n = np.array(T56.subs({theta_6: joint6})).astype(np.float64)

T02_n = T01_n @ T12_n
T03_n = T02_n @ T23_n
T04_n = T03_n @ T34_n
T05_n = T04_n @ T45_n
T06_n = T05_n @ T56_n

# =========================
# 7. Ploteo de frames DH
# =========================
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

trplot(T0,   ax=ax, length=0.15, frame='0', color='k')
trplot(T01_n, ax=ax, length=0.15, frame='1', color='b')
trplot(T02_n, ax=ax, length=0.15, frame='2', color='r')
trplot(T03_n, ax=ax, length=0.15, frame='3', color='g')
trplot(T04_n, ax=ax, length=0.15, frame='4', color='m')
trplot(T05_n, ax=ax, length=0.15, frame='5', color='y')
trplot(T06_n, ax=ax, length=0.15, frame='6', color='c')

# También plotea el frame final calculado desde T06_solved
T06_final = np.array(T06_solved.evalf(), dtype=np.float64)
trplot(T06_final, ax=ax, length=0.18, frame='f', color='purple')

plt.title('Gráfica de transformaciones')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()