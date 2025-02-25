import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
As noted in Prob 1.3, drag is more accurately represented as depending on 
the square of velocity. A more fundamental represetnation of the drag force, 
which assumes turbulent conditions (i.e. a high Reynolds number), can be 
formulated as 

F_{d} = -1/2* rho * A * C_{d} * v * |v|

where F_{d}  = the drag force (N), rho = fluid density (kg/m^{3}), A = the frontal
area of the object on a plane perpendicular to the direction of motion (m^{2}), 
v = velocity (m/s), and C_{d} = a dimensionless drag coefficient.

(a) Write the pair of differential equations for velocity and position (see Prob 1.17)
to describe the vertical motion of a sphere with diameter d (m) and a density rho_{s} (kg/m^{3}). 
The differential equation for velocity should be written as a function of the sphere's diameter.

(b) Use Euler's method with a step size ∆t = 2 s to compute the position and velocity 
of a sphere over the first 14 s. Employ the following parameters in your calculation: d = 125 cm, 
rho = 1.3 kg/m^{3}, rho_{s} = 2650 kg/m^{3}, and C_{d} = 0.475. Assume that the sphere has the
initial conditions y(0) = -100 m and v(0) = -45 m/s. 

(c) Develop a plot of your results (i.e. y and v versus t) and use it to graphically estimate 
when the sphere would hit the ground. 

(d) Compute the value for the bulk second-order drag coefficient c_{d}' (kg/m). Note that as described
in Prob. 1.3, the bulk second-order drag coefficient is the term in the final differential equation for
velocity that multiplies the term v|v|.
"""