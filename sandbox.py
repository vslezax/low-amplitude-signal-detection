import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the Poisson probability mass function
lambda_param = 4
x = np.arange(0, 20, 0.1)  # Define a range for x values

# Poisson PMF as a function of continuous x for visualization
poisson_pmf = lambda x: np.exp(-lambda_param) * np.power(lambda_param, x) / np.math.factorial(int(x)) if x == int(x) else 0

# Vectorized version of PMF for smooth visualization
vectorized_pmf = np.vectorize(poisson_pmf, otypes=[float])
pmf_values = vectorized_pmf(np.round(x))

# First derivative (difference approximation)
first_derivative = np.gradient(pmf_values, x)

# Second derivative
second_derivative = np.gradient(first_derivative, x)

# Plot the function and its derivatives
plt.figure(figsize=(12, 8))
plt.plot(x, pmf_values, label='Poisson PMF (λ=4)', color='blue')
plt.plot(x, first_derivative, label="First Derivative", color='green', linestyle='--')
plt.plot(x, second_derivative, label="Second Derivative", color='red', linestyle=':')
plt.title("Poisson Distribution PMF and Its Derivatives")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid()
plt.show()
