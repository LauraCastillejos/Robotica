import roboticstoolbox as rtb
import numpy as np

#print(f"robotics toolbox version: {rtb._version_}")
#print(f"numpy version: {np._version_}")

robot = rtb.models.DH.Puma560()

q=[0,0,0,0,0,0]

#robot.plot(q, block=True, backend='pyplot')

robot.teach(q)

