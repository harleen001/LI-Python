import numpy as np
import matplotlib.pyplot as plt

# Define the cost function f(x)
def cost_function(x):
    return x**2 - 4*x + 3

# Define the derivative of the cost function f'(x)
def gradient(x):
    return 2*x - 4


# Initialize the model parameter with a random value
x = np.random.randn()

# Set the learning rate
learning_rate = 0.1

# Set the maximum number of iterations
max_iterations = 100

# Initialize the list to store the cost values
cost_values = []

# Iterate until convergence or max iterations
for i in range(max_iterations):
    # Calculate the cost and gradient at the current parameter
    cost = cost_function(x)
    grad = gradient(x)

    # Update the parameter
    x = x - learning_rate * grad

    # Store the cost value
    cost_values.append(cost)

    # Print the progress
    if i % 10 == 0:
        print("Iteration {}: x = {}, cost = {}".format(i, x, cost))

# Plot the cost values
plt.plot(cost_values)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()