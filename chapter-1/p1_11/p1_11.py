import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
Apply the conservaiton of volume (see Prob 1.9) to simulate the level of liquid
in a conical storage tank. The liquid flows in at a sinusoidal rate Q_{in} = 3*sin^{2}(t)
and flows out according to 

Q_{out} = 3*(y - y_{out})^{1.5}, y > y_{out}
Q_{out} = 0                    , y ≤ y_{out}

where flow has units of m^{3}/d and y = the elevation of the water surface above the 
bottom of the tank (m). Use Euler's method to solve for the depth y from t = 0 to 8 d
with a step size of 0.4 d. The parameter values are r_{top} = 2.5 m, y_{top} = 4 m, 
and y_{out} = 1 m. Assume that the level is initially below the outlet pipe with 
y(0) = 0.75 m. 
"""