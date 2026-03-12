import sympy as sp
import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3
import matplotlib.pyplot as plt

# ==========================================================
# 1. PARTE SIMBÓLICA CON SYMPY
# ==========================================================
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols(
    'theta_1 theta_2 theta_3 theta_4 theta_5 theta_6'
)

def DH(theta, d, a, alpha):
    return sp.Matrix([
        [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),  sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
        [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
        [0,              sp.sin(alpha),               sp.cos(alpha),                d],
        [0,              0,                           0,                            1]
    ])

deg = sp.pi / 180

# ==========================================================
# 2. TABLA DH SIMBÓLICA
# ==========================================================
T01 = DH(theta_1,            450, 130, -90*deg)
T12 = DH(theta_2 - 90*deg,     0, 600,   0*deg)
T23 = DH(theta_3,              0, 150, -90*deg)
T34 = DH(theta_4,            760,   0,  90*deg)
T45 = DH(theta_5,              0,   0, -90*deg)
T56 = DH(theta_6,            100,   0,   0*deg)

T06 = sp.simplify(T01 * T12 * T23 * T34 * T45 * T56)

print("\n================ MATRIZ T06 SIMBÓLICA ================\n")
sp.pprint(T06)

valores_juntas = {
    theta_1: 0,
    theta_2: 0,
    theta_3: 0,
    theta_4: 0,
    theta_5: 0,
    theta_6: 0
}

T06_num = sp.N(T06.subs(valores_juntas), 4)

print("\n================ MATRIZ T06 EVALUADA ================\n")
sp.pprint(T06_num)

# ==========================================================
# 3. MODELO DEL ROBOT EN ROBOTICSTOOLBOX
#    Aquí usamos metros para la visualización
# ==========================================================
robot6 = rtb.DHRobot(
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
print(robot6)

# ==========================================================
# 4. CONFIGURACIÓN ARTICULAR
# ==========================================================
q0 = np.array([0, 0, 0, 0, 0, 0])

print("\n================ FKINE CON ROBOTICSTOOLBOX ================\n")
print(robot6.fkine(q0))

# ==========================================================
# 5. GRAFICAR EL ROBOT Y DEJAR LA VENTANA ABIERTA
# ==========================================================
env = robot6.plot(
    q0,
    backend='pyplot',
    limits=[-1.5, 1.5, -1.5, 1.5, -0.2, 1.8],
    shadow=True,
    jointaxes=True,
    block=True
)

# Esto ayuda a mantener la figura abierta al terminar el script
if env is not None:
    env.hold()

plt.show(block=True)

