import numpy as np

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
    temp_vi = 0
    while vf - vi >= 0.001 * vi: 
        vi = temp_vi
        vf = vi + (g - c*vi/m)*step
        temp_vi = vf
    return vf

print(f"Terminal velocity: {v_gen():.2f}")