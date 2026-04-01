import numpy as np
import matplotlib.pyplot as plt

# Define the cost function f(x)
def cost_function(x):
    return x**2 - 4*x + 3

# Define the derivative of the cost function f'(x)
def gradient(x):
    return 2*x - 4

# Define the gradient descent algorithm
def gradient_descent(cost_function, gradient, x_init, alpha, num_iterations):
    x = x_init
    x_list = [x]
    for i in range(num_iterations):
        cost = cost_function(x)
        grad = gradient(x)
        x = x - alpha * gradient(x)
        x_list.append(x)
        # Print the progress
        print("Iteration {}: x = {}, cost = {}".format(i, x, cost))

    return x_list

# Set the hyperparameters
alpha = 0.1
num_iterations = 5

# Run gradient descent on f(x)
x_init = 15
x_list = gradient_descent(cost_function, gradient, x_init, alpha, num_iterations)

# Create an array of x values
x = np.linspace(-2, 15, 100)

# Evaluate f(x) for each value of x
y = cost_function(x)

# Plot f(x) versus x
plt.plot(x, y)

# Plot the gradient descent iterations
for i in range(len(x_list) - 1):
    x1 = x_list[i]
    y1 = cost_function(x1)
    x2 = x_list[i + 1]
    y2 = cost_function(x2)
    plt.plot([x1, x2], [y1, y2], 'ro-')
    plt.text(x1, y1 + 0.5, round(y1, 2))

# Label the final cost value
x_final = x_list[-1]
y_final = cost_function(x_final)
plt.text(x_final, y_final + 0.5, round(y_final, 2))

# Add labels and a title to the plot
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient descent iterations on f(x)')

# Display the plot
plt.show()