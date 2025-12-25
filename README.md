# Tank Level Dynamics

## Overview
This project focuses on dynamic modeling of a liquid tank system using Python. The goal is to translate physical mass balances into differential equations and solve them numerically.

## Objectives
- Develop a dynamic model for tank level behavior
- Solve the governing differential equation using Python
- Visualize system response over time

## Model Description
A dynamic mass balance is applied to a liquid tank system. The governing equation for the liquid level is:

dh/dt = (Qin − Qout) / A

where the outlet flow rate is modeled as:

Qout = c√h

## Modelling Assumptions
- The tank is perfectly mixed and lumped.
- Fluid properties are constant.
- The inlet flow rate is constant in time.
- The outlet flow depends only on the height of liquid above the outlet.
- Effects such as leakage and evaporation are neglected.

## Steady State Analysis
At steady state, the liquid level remains constant and the inlet and outlet flow rates are equal. By setting the time derivative of the tank level to zero, an analytical expression for the steady-state height is obtained.
The numerical simulation converges to this steady-state value, confirming the validity of the dynamic model.

## Model Versions
**Version 1 (V1):**  
Base dynamic tank level model with analytical steady-state validation.

**Version 2 (V2):**  
A disturbance is applied to the inlet flow rate at a specified time, and the resulting transient response and new steady state are analyzed.
  
## Numerical Method
The ordinary differential equation is solved numerically using SciPy’s solve_ivp function, with the solution evaluated at uniformly spaced time points for plotting.

## Results and Visualization
The model outputs the liquid level as a function of time, which is plotted to observe the transient and steady-state behavior of the tank system.

## Tools Used
- Python
- NumPy
- SciPy
- Matplotlib
  
## References
- [1] Aleksandar Haber PhD, “Derivation of Dynamics of Tank Filled with Fluid and Python Simulation - Control and Process Dynamic,” YouTube, May 10, 2024. https://www.youtube.com/watch?v=TBkTAmOu9Io (accessed Dec. 24, 2025).
- [2] M. Pathak, “A Practical Guide to scipy.integrate.solve_ivp - AskPython,” AskPython, Jul. 2025. https://www.askpython.com/python-modules/scipy/scipy-integrate-solve_ivp (accessed Dec. 24, 2025).
