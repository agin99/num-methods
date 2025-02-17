import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
For the free falling parachutist with linear drag, assume a first
jumper is 70 kg and has a drag coefficient of 12 kg/s. If the second jumper has a drag
coefficient of 15 kg/s and a mass of 75 kg, how long will it take him to reach the same
velocity as the first jumper reached in 10s?
"""

g = 9.8 #m/s^2
m1 = 70 #kg
c1 = 12 #kg/s 
m2 = 75 #kg
c2 = 15 #kg/s

def v_gen(mass, drag, step):
    vi = 0
    vf = g*step
    v_list = []
    temp_vi = 0
    while vf - vi >= 0.0000001 * vi: 
        vi = temp_vi
        vf = vi + (g - drag*vi/mass)*step
        v_list.append(vf)
        temp_vi = vf
    return vf, v_list

v1f, v1_list = v_gen(m1, c1, 1)
v2f, v2_list = v_gen(m2, c2, 1)
v_target = v1_list[9]
v2_index = 0 
for index, v in enumerate(v2_list):
    if v >= v_target:
        v2_index = index
        break
print(v2_index, v2_list[v2_index], v_target)
plt.plot([i for i in range(len(v1_list))], v1_list, 'green', label='70kg, 12kg/s drag')
plt.plot([i for i in range(len(v2_list))], v2_list, 'red', label='75kg, 15kg/s drag')
plt.legend()
plt.savefig('p1_4.png')