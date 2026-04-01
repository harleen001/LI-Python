# Import necessary libraries
import numpy as np

# Define the cost function f(x)
def cost_function(x):
    return x**2 - 4*x + 3

# Define the derivative of the cost function f'(x)
def gradient(x):
    return 2*x - 4

# Gradient Descent parameters
learning_rate = 0.1  # Step size
iterations = 20     # Number of iterations

# Initial guess for x (starting point)
x = 0.0

# Gradient Descent optimization
for i in range(iterations):
    # Compute the gradient at the current point
    grad = gradient(x)

    # Update x using the Gradient Descent formula
    x = x - learning_rate * grad

# The value of x after optimization represents the minimum of the cost function
minimum_x = x
minimum_cost = cost_function(minimum_x)

# Print the result
print(f"Minimum value of x: {minimum_x}")
print(f"Minimum cost: {minimum_cost}")

import math

# Print the result
print(f"Minimum value of x: {math.ceil(minimum_x)}")
print(f"Minimum cost: {math.floor(minimum_cost)}")