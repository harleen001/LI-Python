import numpy as np

# A simple linear regression hypothesis function
def linear_hypothesis(X, weights):
    """
    Calculates the predicted output for a linear model.

    Args:
        X (numpy.ndarray): Input features (e.g., a matrix where each row is a sample).
        weights (numpy.ndarray): Model parameters (e.g., coefficients and intercept).

    Returns:
        numpy.ndarray: Predicted outputs.
    """
    # Assuming the last element of weights is the intercept
    # and the preceding elements are coefficients for features
    return np.dot(X, weights[:-1]) + weights[-1]

# Example usage:
# Sample input features (e.g., house size)
X_train = np.array([[100], [150], [200], [250]])

# Initial or learned weights (coefficient for size, and intercept)
# Let's say we learned a model: price = 2 * size + 50
learned_weights = np.array([2, 50])

# Make predictions using the hypothesis
predictions = linear_hypothesis(X_train, learned_weights)
print("Predictions:", predictions)