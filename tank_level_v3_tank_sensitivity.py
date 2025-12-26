import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Parameters
A = 1.0
Qin = 0.5
c_nominal = 0.3
c_restrictive = 0.2

#Tank level calculation
def tank_level(t,h,c):
    Qout = c*np.sqrt(h)
    dh_dt = (Qin - Qout)/A
    return dh_dt

Time_span = (0,60)
num_points = 300
h0 = [0.2] #Initial height

#Simulations
soln_nominal = solve_ivp(tank_level, Time_span, h0, args=(c_nominal,), dense_output=True) #Nominal valve
soln_restrictive = solve_ivp(tank_level, Time_span, h0, args=(c_restrictive,), dense_output=True) #Restrictive valve

#Processing
t = np.linspace(Time_span[0], Time_span[1], num_points)
h_nominal = soln_nominal.sol(t)[0]
h_restrictive = soln_restrictive.sol(t)[0]

#Analysis of steady state
h_ss_nominal = (Qin/c_nominal)**2
h_ss_restrictive = (Qin/c_restrictive)**2

#Plotting
plt.figure()
plt.plot(t, h_nominal, label = 'c = 0.3 (Nominal)')
plt.plot(t, h_restrictive, label = 'c = O.2 (Restrictive)')
plt.ylabel("Tank Level (m)")
plt.xlabel("Time (s)")
plt.axhline(h_ss_nominal, linestyle = '--', color='red', label = 'Nominal Steady State')
plt.axhline(h_ss_restrictive, linestyle='--', color='black', label='Restrictive Steady State')
plt.title("Valve Coefficient Sensitivity: Tank Level Dynamics")
plt.legend()
plt.grid()
plt.show()
