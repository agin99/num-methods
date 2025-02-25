import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
You are working as a crime-scene investigator and must predict the temperature 
of a homicide victim over a 5-hr period. You know that the room where the victim
was found was at 12 C when the body was discovered. 

(a) Use Newton's law of cooling (Prob 1.14) and Euler's method to compute the
victim's body temperature for the 5-hr period using values of k=0.12/hr and 
∆t = 0.5 hr. Assume that the victim's body temperature at the time of death was 37 C
and that the room temperature was at a constant value of 12 C over the 5-hr period. 

(b) Further investigation reveals that the room temperature had actually dropped 
linearly from 20 to 12 C over the 5-hr period. Repeat the same calculation as in (a)
but incorportate this new information. 

(c) Compare the results from (a) and (b) by plotting them in the same graph.
"""