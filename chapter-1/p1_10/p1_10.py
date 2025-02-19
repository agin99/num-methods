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

