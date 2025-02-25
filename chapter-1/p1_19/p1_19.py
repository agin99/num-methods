import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
Suppose that a parachutist with linear drag (m = 70kg, c = 12.5 kg/s) jumps 
from an airplane flying at an altitude of 200 m with a horizontal velocity of 
180 m/s relative to the ground. 

(a) Write a system of four differential equation for x, y, v_{x} = dx/dt, and 
v_{y} = dy/dt. 

(b) If the initial horizontal position is defined as x=0, use Euler's methods with 
∆t = 1s to compute the jumper's position over the first 10s.

(c) Develop plots of y versus t and y versus x. Use the plots to graphically estimate 
when and where the jumper would hit the ground if the chute failed to open. 

(d) At what angle would the parachutist be traveling in the last whole second before
impact? 
"""