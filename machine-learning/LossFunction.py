import numpy as np

def mean_squared_error(y_true, y_pred):
    """Calculates Mean Squared Error."""
    return np.mean((y_true - y_pred)**2)

def mean_absolute_error(y_true, y_pred):
    """Calculates Mean Absolute Error."""
    return np.mean(np.abs(y_true - y_pred))

# Example usage
y_true = np.array([1, 2, 3, 4])
y_pred = np.array([1.5, 2.2, 2.8, 4.1])

mse_loss = mean_squared_error(y_true, y_pred)
mae_loss = mean_absolute_error(y_true, y_pred)

print(f"MSE Loss: {mse_loss}")
print(f"MAE Loss: {mae_loss}")