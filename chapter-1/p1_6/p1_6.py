import numpy as np
import matplotlib.pyplot as plt
"""
Problem statement: 
The following information is available for a bank account: 
---------------------------------------------------
Date | Deposits | Withdrawals | Interest | Balance 
5/1  |          |             |          | 1512.33
     | 220.13   | 327.26      |          | 
6/1  |          |             |          |
     | 216.80   | 378.61      |          | 
7/1  |          |             |          |
     | 450.25   | 106.80      |          | 
8/1  |          |             |          |
     | 127.31   | 350.61      |          | 
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

deposits = [220.13, 216.80, 450.25, 127.31]
withdrawals = [327.26, 378.61, 106.80, 350.61]

def compute_balance(starting_balance, rate): 
    balances = [starting_balance]
    interest_earned = [0]
    for deposit, withdrawal in zip(deposits, withdrawals):
        interest = balances[-1] * (rate)
        interest_earned.append(interest)
        balances.append(balances[-1] + interest + deposit - withdrawal)
    return balances, interest_earned

def simulate_acc_balance(starting_balance, rate, step): 
    balances = [starting_balance]
    t = [0]
    index = 0
    while np.floor(index) < len(deposits):
        effective_index = int(np.floor(index))
        balances.append(balances[-1] + (deposits[effective_index] - withdrawals[effective_index] + rate*balances[-1])*step)
        index += step
        t.append(index)
    return t, balances

final_balances, interest_earned = compute_balance(1512.33, 0.01)
t, balances = simulate_acc_balance(1512.33, 0.01, 0.5)
print("\n(a)")
for index, balance in enumerate(final_balances):
    print(f"Balance on {5+index}/1: {balance:.2f}")

print("\n(c)")
for time, balance in zip(t, balances):
    print(f"Balance on {time}: {balance:.2f}")


plt.xlabel("Time (t)")
plt.ylabel("Account Balance B(t)")
t1 = np.linspace(0, 5, 5)
plt.ylim(0, 2000)
plt.plot(t1, final_balances, 'green')
plt.plot(t, balances, 'red')
plt.savefig('p1_6.png')
plt.show()
