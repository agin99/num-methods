import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
As depicted in Fig. P1.15, an RLC circuit consists of three elements: a 
resistor (R), an inductor (L), and a capacitor (C). The flow of current 
across each element induces a voltage drop. Kirchhoff's second voltage law 
states that the algebraic sum of these voltage drops around a closed circuit
is zero, 

iR + L di/dt + q/C = 0

where i = current, R = resistance, L = inductance, t = time, q = charge, 
and C = capacitance. In addition, the current is related to charge as in 

dq/dt = i 

(a) If the initial values are i(0) = 0 and q(0) = 0.5 C, use Euler's method to 
solve this pair of differential equations from t = 0 to 0.1 s using a step size of 
∆t = 0.01 s. Employ the following parameters for your calculation: R = 250 ohms, 
L = 5 H, and C = 10^{-4} F. 

(b) Develop a plot of i and q versus t.
"""