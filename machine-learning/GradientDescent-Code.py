import numpy as np

def gradient_descent(X, y, learning_rate, iterations):
    m, n = X.shape
    weights = np.zeros(n)
    bias = 0

    for i in range(iterations):
        # Calculate predictions
        predictions = np.dot(X, weights) + bias

        # Calculate errors
        errors = predictions - y

        # Calculate gradients
        gradient_weights = (1/m) * np.dot(X.T, errors)
        gradient_bias = (1/m) * np.sum(errors)

        # Update weights and bias
        weights = weights - learning_rate * gradient_weights
        bias = bias - learning_rate * gradient_bias

    return weights, bias

# Example usage
X = np.array([[1, 2], [2, 3], [3, 4]])
y = np.array([3, 5, 7])
learning_rate = 0.01
iterations = 1000

weights, bias = gradient_descent(X, y, learning_rate, iterations)
print(f"Learned Weights: {weights}, Learned Bias: {bias}")