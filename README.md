# Lorenz Attractor

![DLA](lorenz.png)


The Lorenz system was first introduced by Edward Lorenz, an American mathematician and meteorologist, in 1963. Lorenz was studying weather patterns and atmospheric convection when he stumbled upon what would later be recognized as one of the earliest and most famous examples of chaotic systems. His work not only revolutionized weather forecasting but also played a pivotal role in the development of chaos theory.  

Overview  
This project implements a mathematical model known as the Lorenz system, a set of three coupled, first-order, nonlinear differential equations originally developed to model atmospheric convection. The system is famous for producing chaotic solutions that are highly sensitive to initial conditions, a concept often referred to as the "butterfly effect." Small changes in initial conditions can lead to vastly different outcomes, making long-term prediction impossible in practical terms.  

The system's equations are as follows:

$$
\begin{aligned}
\frac{dx}{dt} &= \sigma (y - x) \\
\\
\frac{dy}{dt} &= x (\rho - z) - y \\
\\
\frac{dz}{dt} &= x y - \beta z
\end{aligned}
$$

Where:

x, y, z are the system's state variables,
σ (sigma), ρ (rho), and β (beta) are the system's parameters.
The Lorenz system is a simplified model for atmospheric convection and exhibits chaotic behavior for certain parameter values, making it one of the most famous examples of chaotic systems in physics and mathematics.

Parameters  

σ (sigma): The Prandtl number, which measures the ratio of momentum diffusivity to thermal diffusivity.
ρ (rho): The Rayleigh number, which controls the convection strength.
β (beta): The ratio of the system's physical dimensions.
How It Works

The Lorenz system is solved numerically using initial conditions and the specified parameter values. The system's chaotic behavior becomes apparent when small changes in initial conditions lead to drastically different outcomes over time. This property is often referred to as the butterfly effect.

Numerical Solution  

The system of differential equations is solved numerically using a method like Runge-Kutta or odeint (in Python's scipy.integrate library), which computes the values of x, y, and z at each time step. By iterating over time, the behavior of the system is observed.