# Lorenz Attractor

This project implements a mathematical model known as the Lorenz system, which is a set of three coupled, first-order, nonlinear differential equations originally developed to model atmospheric convection.

Overview

The Lorenz system is famous for its chaotic solutions, which are highly sensitive to initial conditions. The system's equations are as follows:

$$
\[
\frac{dx}{dt} = \sigma (y - x)
\]

\[
\frac{dy}{dt} = x (\rho - z) - y
\]

\[
\frac{dz}{dt} = x y - \beta z
\]
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