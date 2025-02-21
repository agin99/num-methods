import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
For the same storage tank described in Prob 1.9, suppose that the outflow is 
not constant but rather depends on the depth. For this case, the differential 
equation for depth can be written as 

dy/dt = 3 Q/A sin^{2}(t) - (a(1+y)^{1.5})/A

Use Euler's method to solve for the depth y from t = 0 to 10 d with a step
size of 0.5d. The parameter values are A = 1200 m^{2}, Q = 500 m^{3}/d, and
a = 150. Assume that the initial condition is y = 0. 
"""

def tank_depth(alpha, A, Q, end, step):
    times = [0]
    y_depths = [0]
    while times[-1] < end:
        y_i = y_depths[-1]
        y_f = (3 * Q / A * np.sin(times[-1])**2  - alpha * (1 + y_i)**1.5 / A) * step + y_i
        y_depths.append(float(y_f))
        times.append(times[-1] + step)
    return times, y_depths

times, y_depths = tank_depth(150, 1200, 500, 10, 0.5)
plt.xlabel('Time (t)')
plt.ylabel('Depth Relative to Half Full (y(t))')
plt.plot(times, y_depths)
plt.savefig('p1_10.png')
plt.show()