import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def lorenz(t, y, sigma, rho, beta):
    """Lorenz system of differential equations."""
    dx = sigma * (y[1] - y[0])
    dy = y[0] * (rho - y[2]) - y[1]
    dz = y[0] * y[1] - beta * y[2]
    return [dx, dy, dz]

def solve_lorenz(sigma=10, rho=28, beta=8/3, t_end=100, num_points=10000):
    """Solve the Lorenz system using SciPy's solve_ivp."""
    t_span = (0, t_end)
    t_eval = np.linspace(*t_span, num_points)                          
    y0 = [0.5, 0.5, 0.5]

    sol = solve_ivp(lorenz, t_span, y0, t_eval=t_eval, args=(sigma, rho, beta))
    
    return sol.t, sol.y

def plot_lorenz(sigma=10, rho=28, beta=8/3, t_end=100, num_points=10000):
    """Solve and plot the Lorenz attractor."""
    t, y = solve_lorenz(sigma, rho, beta, t_end, num_points)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(y[0], y[1], y[2], lw=0.5)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title(f"Lorenz Attractor (σ={sigma}, ρ={rho}, β={beta})")

    plt.show()

plot_lorenz()
