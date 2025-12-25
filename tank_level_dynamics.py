import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Parameters
A = 1.0
Qin = 0.5
c = 0.3

#Tank level calculation
def tank_level(t,h):
    Qout = c*np.sqrt(h)
    dh_dt = (Qin - Qout)/A
    return dh_dt

Time_span = (0,60)
num_points = 300
h0 = [0.2] #Initial height

soln = solve_ivp(tank_level, Time_span, h0, dense_output=True) #Numerical computation

#Processing
t = np.linspace(Time_span[0], Time_span[1], num_points)
h = soln.sol(t)[0]

#Creating a steadystate option
h_ss = (Qin/c)**2

#Plotting
plt.figure()
plt.plot(t,h)
plt.ylabel("Tank Level (m)")
plt.xlabel("Time (s)")
plt.axhline(h_ss, linestyle = '--', color='red', label = 'Steady State')
plt.title("Dynamic Tank Level Response")
plt.legend()
plt.grid()
plt.show()
