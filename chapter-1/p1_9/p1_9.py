import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
A storage tank contains a liquid at depth y, where y = 0 when the tank 
is half full (Fig. P1.9). Liquid is withdrawan at a constant flow rate
Q to meet demands. The contents are resupplied at a sinusoidal rate 3Qsin^{2}(t).
Equation (1.13) can be written for this system as 

d(Ay)/dt = 3Qsin^{2}(t) - Q
(change in volume) = (inflow) - (outflow)

or, since the surface area A is constant, 

dy/dt = 3 Q/A sin^{2}(t) - Q/A 

Use Euler's method to solve for the depth y from t = 0 to 10 d with a 
step size of 0.5 d. The parameter values are A = 1200 m^{2} and 
Q = 500 m^{3}/d. Assume that the initial condition is y = 0. 
"""

def tank_depth(A, Q, end, step):
    times = [0]
    y_depths = [0]
    while times[-1] < end:
        y_i = y_depths[-1]
        y_f = (3 * Q / A * np.sin(times[-1])**2  - Q / A) * step + y_i
        y_depths.append(float(y_f))
        times.append(times[-1] + step)
    return times, y_depths

times, y_depths = tank_depth(1200, 500, 10, 0.5)
plt.xlabel('Time (t)')
plt.ylabel('Depth Relative to Half Full (y(t))')
plt.plot(times, y_depths)
plt.savefig('p1_9.png')
plt.show()
