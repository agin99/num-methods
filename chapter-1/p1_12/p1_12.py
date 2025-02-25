import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
In our example of the free-falling parachutist, we assumed that the acceleration 
due to gravity was a constant value. Although this is a decent approximation when 
we are examining falling objects near the surface of the earth, the gravitational 
force decreases as we move above sea level. A more general representation based on 
Newton's inverse square law of gravitational attraction can be written as 

g(x) = g(0)*(R^{2} / (R + x)^{2})

where g(x) = gravitational acceleration at altitude x (in m) measured upward from 
the earth's surface (m/s^{2}), g(0) = gravitational acceleration at the earth's 
surface (\cong 9.81 m/s^{2}), and R = the earth's radius (\cong 6.37 x 10^{6} m).

(a) In a fashion similar to the derivation of Eq. (1.9), use a force balance to 
derive a differential equation for velocity as a function of time that utilizes 
this more complete representation of gravitation. However, for this derivation,
assume that upward velocity is positive.

(b) For the case where drag is negligible, use the chain rule to express the differential
equation as a function of altitude rather than time.

(c) Use calculus to obtain the closed-form solution where v=v_{0} at x=0. 

(d) Use Euler's method to obtain a numerical solution from x=0 to 100,000 m using a step 
size of 10,000 m where the initial velocity is 1400 m/s upward. Compare your result with
the analytical solution. 
"""