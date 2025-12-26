import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#Parameters
A = 1.0
Qin_nominal = 0.5
disturbance_fraction = 0.6 #how much disturbance affected the tank
t_disturbance = 40 #time of disturbance
c = 0.3
Qin_disturbed = Qin_nominal * (1 + disturbance_fraction)
#Tank level calculation
def tank_level(t,h):
    if t<t_disturbance:
        Qin = Qin_nominal
    else:    
        Qin = Qin_disturbed
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
h_ss1 = (Qin_nominal/c)**2
h_ss2 = (Qin_disturbed/c)**2

#Plotting
plt.figure()
plt.plot(t,h)
plt.ylabel("Tank Level (m)")
plt.xlabel("Time (s)")
plt.axhline(h_ss1, linestyle = 'solid', color='green', label = 'Nominal Steady State')
plt.axhline(h_ss2, linestyle = '--', color='red', label = 'Steady State after Disturbance')
plt.axvline(t_disturbance, linestyle = ':', color = 'black', label = 'Time of Disturbance')
plt.title("Dynamic Tank Level Response")
plt.legend()
plt.grid()
plt.show() 
