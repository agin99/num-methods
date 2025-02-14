import numpy as np
import matplotlib.pyplot as plt

"""
Problem statement: A parachutist of mass 68.1 kg jumps out of a stationary
hot air balloon. Use 

v(t) = gm/c x (1 - e^{-(c/m)t})

to compute velocity prior to opening the chute. The drag coefficient is equal to 12.5 kg/s. 
Employ a step size of 2s for the calculation. 

g := acceleration of gravity
m := mass of the parachutist
c := drag coefficient
"""
g = 9.8 #m/s^2
m = 68.1 #kg
c = 12.5 #kg/s 
step = 2 #s

def v_gen():
    vi = 0
    vf = g*step
    v_list = []
    temp_vi = 0
    while vf - vi >= 0.0000001 * vi: 
        vi = temp_vi
        vf = vi + (g - c*vi/m)*step
        v_list.append(vf)
        temp_vi = vf
    return vf, v_list

v_t, v_list = v_gen()
t = [2*i for i in range(len(v_list))]

plt.xlabel("Time t")
plt.ylabel("Velocity v(t)")
plt.text(45, 50, f"Terminal velocity: {v_t:.2f}")
plt.plot(t, v_list)
plt.savefig("v_plot.png")
plt.show()