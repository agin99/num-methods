import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
Newton's law of cooling says that the temperature of a body changes at a rate 
proportional to the difference between its temperature and that of the surrounding
medium (the ambient temperature), 

dT/dt = -k(T - T_{a})

where T = the temperature of the body (degrees celsius), t = time (min), 
k = the proportionality constant (per minute), and T_{a} = the ambient temperature
(degrees celsius). Suppose that a cup of coffee originally has a temperature of 
68 C. Use Euler's method to compute the temperature from t=0 to 10 min using a step
size of 1 min if T_{a} = 21 C and k = 0.019/min. 
"""