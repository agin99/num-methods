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

def v_gen(step):
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

v1_t, v1_list = v_gen(2)
t1 = [2*i for i in range(len(v1_list))]

v2_t, v2_list = v_gen(10)
t2 = [2*i for i in range(len(v2_list))]

v3_t, v3_list = v_gen(1)
t3 = [2*i for i in range(len(v3_list))]

v4_t, v4_list = v_gen(0.5)
print(len(v4_list))
t4 = [2*i for i in range(len(v4_list))]

plt.xlabel("Time t")
plt.ylabel("Velocity v(t)")
plt.plot(t1, v1_list, 'green', label=f"2s: TV = {v1_t:.2f}")
plt.plot(t2, v2_list, 'orange', label=f"10s: TV = {v2_t:.2f}")
plt.plot(t3, v3_list, 'red', label=f"1s: TV = {v3_t:.2f}")
plt.plot(t4, v4_list, 'blue', label=f"0.5s: TV = {v4_t:.2f}")
plt.legend()
plt.savefig("p1_2.png")

