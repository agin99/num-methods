import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
The following information is available for a bank account: 
---------------------------------------------------
Date | Deposits | Withdrawals | Interest | Balance 
5/1  | 220.13   | 327.26      |          | 1512.33
6/1  | 216.80   | 378.61      |          |
7/1  | 450.25   | 106.80      |          |
8/1  | 127.31   | 350.61      |          |
9/1  |          |             |          |
---------------------------------------------------
Note that the money earns interest, which is computed as
Interest = iB_{i}
where i = the interest rate expressed as a fraction per month
B_{i=the initial balance at the beginning of the month}.
(a) Use the conservation of cash to compute the balance on 6/1,
    7/1, 8/1, and 9/1 if the interest rate is 1% per month (i = 
    0.01/month). Show each step in the computation. 
(b) Write a differential equation for the cash balance in the form 
    dB/dt = f(D(t), W(t), i)
    where t = time (months), D(t) = deposits as a function of time ($/month),
    W(t) = withdrawals as a function of time ($/month). For this case, assume 
    that interest is compounded continuously; that is, interest = iB.
(c) Use Euler's method with a time step of 0.5 month to simulate the balance. 
    Assume that the deposits and withdrawals are applied uniformly over the
    month.
(d) Develop a plot of balance versus time for (a) and (c).
"""
