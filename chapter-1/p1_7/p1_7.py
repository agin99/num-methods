import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
The amount of a uniformly distributed radioactive contaminant contained in a
closed reactor is measured by its concentration c (becquerel/liter, or Bq/L). 
The contaminant decreases at a decay rate proportional to its concentration-
that is, 

decay rate = -kc 

where k is a constant with units of day^{-1}. Therefore, according to Eq. (1.13),
a mass balance for the reactor can be written as 

dc/dt = -kc 
(change in mass) = (decrease by decay)

(a) Use Euler's method to solve this equation from t=0 to 1d with k = 0.2 d^{-1}. Employ
a step size of (\delta t) = 0.1. The concentration at t=0 is 10 Bq/L. 
(b) Plot the solution on a semilon graph (i.e. ln c versus t) and determine the slope.
Interpret your results.
"""