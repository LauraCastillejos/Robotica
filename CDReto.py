import numpy as np
import roboticstoolbox as rtb
from spatialmath import SE3
import matplotlib.pyplot as plt

# ==========================================
# 1. Definir robot con parámetros DH
# ==========================================
robot = rtb.DHRobot([
    rtb.RevoluteDH(d=0.450, a=0.130, alpha=-np.pi/2),
    rtb.RevoluteDH(d=0.000, a=0.600, alpha=0.0),
    rtb.RevoluteDH(d=0.000, a=0.150, alpha=-np.pi/2),
    rtb.RevoluteDH(d=0.760, a=0.000, alpha=np.pi/2),
    rtb.RevoluteDH(d=0.000, a=0.000, alpha=-np.pi/2),
    rtb.RevoluteDH(d=0.100, a=0.000, alpha=0.0)
], name="Robot_6GDL", base=SE3(), tool=SE3())

print(robot)

# ==========================================
# 2. Poses articulares en grados
# ==========================================
poses_deg = {
    "P1":  [-67.17,  -28.262, 142.747, 99.897, 69.322,   61.679],
    "P2":  [-73.224,  -5.543, 125.317, 98.514, 75.491,   57.115],
    "P3":  [-79.82,   43.938,  63.307, 93.047, 80.283, -289.531],
    "P4":  [-79.153,  44.282,  62.776, 93.217, 79.635, -289.377],
    "P5":  [-79.82,   43.938,  63.307, 93.047, 80.283, -289.531],
    "P6":  [-61.429, -43.557, 151.007, 99.275, 62.856, -291.72 ],
    "P7":  [ 36.175, -12.186, 149.182,  0.000, 43.005, -143.825],
    "P8":  [ 23.001,  15.799, 125.018,  0.000, 39.183,  -66.999],
    "P9":  [ 23.001,  18.2,   125.327,  0.000, 36.473,  -66.999],
    "P10": [  1.779, -38.032, 124.577,  0.000, 93.455,  -88.221],
    "P11": [-67.17,  -28.262, 142.747, 99.897, 69.322,   61.679]
}

# ==========================================
# 3. Cinemática directa para cada pose
# ==========================================
resultados = {}

for nombre_pose, angulos_deg in poses_deg.items():
    q_rad = np.deg2rad(angulos_deg)   # convertir a radianes
    T = robot.fkine(q_rad)            # cinematica directa
    resultados[nombre_pose] = T

# ==========================================
# 4. Mostrar resultados
# ==========================================
for nombre_pose, T in resultados.items():
    print(f"\n========== {nombre_pose} ==========")
    print("Matriz homogénea T06:")
    print(np.array(T))

    pos = T.t
    print(f"Posición del efector final:")
    print(f"x = {pos[0]:.4f} m")
    print(f"y = {pos[1]:.4f} m")
    print(f"z = {pos[2]:.4f} m")

# ==========================================
# 5. Graficar una pose específica
#    (ejemplo: P1)
# ==========================================
pose_a_graficar = "P1"
q_plot = np.deg2rad(poses_deg[pose_a_graficar])

robot.plot(
    q=q_plot,
    backend='pyplot',
    block=True,
    jointaxes=True,
    shadow=True
)