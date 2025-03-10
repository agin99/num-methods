import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
Suppose that a spherical droplet of liquid evaporates at a rate that is 
proportional to its surface area, 

dV/dt = -kA 

where V = volume (mm^{3}), t = time (min), k = the evaporation rate (mm/min), 
and A = surface area (mm^{2}). Use Euler's method to compute the volume of the
droplet from t=0 to 10 min using a step size of 0.25 min. Assume that k = 0.1 mm/min
and that the droplet initially has a radius of 3 mm. Assess the validity of your
results by determining the radius of your final computed volume and verifying 
that it is consistent with evaporation rate.
"""