import sympy as sp
import numpy as np

# ==============================
# 1. Definir símbolos
# ==============================
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = sp.symbols(
    'theta_1 theta_2 theta_3 theta_4 theta_5 theta_6'
)

# ==============================
# 2. Matriz DH estándar
# ==============================
def DH(theta, d, a, alpha):
    return sp.Matrix([
        [sp.cos(theta), -sp.sin(theta)*sp.cos(alpha),  sp.sin(theta)*sp.sin(alpha), a*sp.cos(theta)],
        [sp.sin(theta),  sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha), a*sp.sin(theta)],
        [0,              sp.sin(alpha),               sp.cos(alpha),                d],
        [0,              0,                           0,                            1]
    ])

# ==============================
# 3. Parámetros DH de tu tabla
#    (trabajando en mm y radianes)
# ==============================

# Conversión de grados a radianes
deg = sp.pi / 180

# Tabla DH
T01 = DH(theta_1,         450, 130, -90*deg)
T12 = DH(theta_2 - 90*deg, 0, 600,   0*deg)
T23 = DH(theta_3,           0, 150, -90*deg)
T34 = DH(theta_4,         760,   0,  90*deg)
T45 = DH(theta_5,           0,   0, -90*deg)
T56 = DH(theta_6,         100,   0,   0*deg)

# ==============================
# 4. Cinemática directa
# ==============================
T06 = sp.simplify(T01 * T12 * T23 * T34 * T45 * T56)

print("\nMatriz T06 simbólica:")
sp.pprint(T06)

# ==============================
# 5. Evaluación numérica
#    Ejemplo: todas las juntas en 0°
# ==============================
valores_juntas = {
    theta_1: 0,
    theta_2: 0,
    theta_3: 0,
    theta_4: 0,
    theta_5: 0,
    theta_6: 0
}

T06_num = sp.N(T06.subs(valores_juntas), 4)

print("\nMatriz T06 evaluada con todas las juntas en 0°:")
sp.pprint(T06_num)