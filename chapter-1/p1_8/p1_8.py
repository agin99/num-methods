import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
A group of 35 students attend a class in a room that measures 11m by 8m by 3m. 
Each student takes up about 0.075 m^3 and gives out about 80W of heat (1W = 1J/s). 
Calculate the air temperature rise during the first 15 minutes of the class
if the room is completely sealed and insulated. Assume the heat capacity, C_{v}, for 
air is 0.718 kJ(kg K). Assume air is an ideal gas at 20ºC and 101.325 kPa. Note that 
heat absorbed by the air Q is related to the mass of the air m, the heat capacity, 
and the change in temperature by the following relationship: 

Q = m \int_{T_{1}}^{T_{2}} C_{v}dT = mC_{v}(T_{2} - T_{1})

The mass of air can be obtained from the ideal gas law: 
PV = frac{m}{Mwt}RT 

where P is the gas pressure, V is the volume of the gas, Mwt is the molecular 
weight of the gas (for air, 28.97 kg/kmol), and R is the ideal gas constant [8.314 kPa m^{3}/(kmol K)].
"""

