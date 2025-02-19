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

