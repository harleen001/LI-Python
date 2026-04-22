import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Kernel Function (e.g., Gaussian Kernel)
def gaussian_kernel(point, x_data, tau):
    """
    Computes weights for data points based on their distance from the query point.
    tau is the bandwidth parameter, controlling the decay rate of weights.
    """
    m = x_data.shape[0]
    weights = np.eye(m)  # Initialize a diagonal matrix for weights
    for i in range(m):
        diff = point - x_data[i]
        weights[i, i] = np.exp(-(diff @ diff.T).item() / (2 * tau ** 2))
    return weights

# 2. Fit the LWLR Model for a single query point
def lwlr(query_point, x_train, y_train, tau):
    """
    Calculates the parameters (theta) of the locally weighted linear model
    and makes a prediction for the query_point.
    """
    x_train_mat = np.asmatrix(x_train)
    y_train_mat = np.asmatrix(y_train).T

    # Add a bias term (intercept) to x_train_mat if not already present
    if x_train_mat.shape[1] == 1: # Assuming x_train is 1D
        x_train_mat = np.hstack((np.ones((x_train_mat.shape[0], 1)), x_train_mat))
        # Ensure query_point is 2D for hstack
        query_point = np.hstack((np.ones((query_point.shape[0], 1)), query_point))

    weights = gaussian_kernel(query_point, x_train_mat, tau)

    # Calculate theta (parameters) using the weighted least squares formula
    theta = (x_train_mat.T * weights * x_train_mat).I * (x_train_mat.T * weights * y_train_mat)

    # Make the prediction
    prediction = query_point * theta
    return prediction

# 3. Predict for multiple query points
def predict_lwlr(x_train, y_train, query_points, tau):
    """
    Generates predictions for an array of query points.
    """
    predictions = []
    for point in query_points:
        # Ensure point is a 2D array (1, n_features) before passing to lwlr
        prediction = lwlr(point.reshape(1, -1), x_train, y_train, tau)
        predictions.append(prediction.item()) # .item() to extract scalar from matrix
    return np.array(predictions)

# 4. Example Usage
if __name__ == "__main__":
    # Generate some sample data
    np.random.seed(0)
    X = np.sort(5 * np.random.rand(100, 1), axis=0)
    y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

    # Define query points for prediction
    X_test = np.linspace(0, 5, 100).reshape(-1, 1)

    # Set the bandwidth parameter (tau)
    tau = 0.1

    # Make predictions
    y_pred = predict_lwlr(X, y, X_test, tau)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.scatter(X, y, label='Training Data', s=20)
    plt.plot(X_test, y_pred, color='red', label=f'LWLR Prediction (tau={tau})')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.title('Locally Weighted Linear Regression')
    plt.legend()
    plt.grid(True)
    plt.show()
