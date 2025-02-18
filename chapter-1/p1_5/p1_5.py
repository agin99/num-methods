import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
Compute the velocity of a parachutist using Euler's method for the case where m = 80kg 
and c = 10 kg/s. Perform the calculation from t = 0 to 20s with a step size of 1s. Use 
an initial condition that the parachutist has an upward velocity of 20m/s at t = 0. At 
t = 10s, assume that the chute is instantenously deployed so that the drag coefficient
jumps to 50 kg/s.
"""

g = 9.8 #m/s^2
m = 80 #kg
c = 10 #kg/s 

def v_gen(mass, drag, step):
    vi = -20
    vf = g*step
    v_list = []
    temp_vi = 0
    time = 0
    while time < 20:
        if time >= 10:
            drag = 50 
        vi = temp_vi
        vf = vi + (g - drag*vi/mass)*step
        v_list.append(vf)
        temp_vi = vf
        time += step
    return vf, v_list

vf, v_list = v_gen(m, c, 1)
plt.xlabel("Time t")
plt.ylabel("Velocity v(t)")
t = np.linspace(0, 20, 20)
plt.plot(t, v_list, 'green')
plt.savefig('p1_5.png')