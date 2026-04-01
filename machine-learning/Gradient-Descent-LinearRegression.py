import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Generate Synthetic Data (Replacing pd.read_csv)
np.random.seed(42)
X = np.array(np.random.rand(100) * 100)  # 100 random points between 0 and 100
# Create Y based on Y = 2X + 5 with some random noise
Y = np.array(2 * X + 5 + np.random.randn(100) * 20)

# 2. Building the model
m = 0
c = 0

L = 0.0001  # The learning Rate
epochs = 1000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# 3. Performing Gradient Descent
for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c

print(f"Final Slope (m): {m}")
print(f"Final Intercept (c): {c}")

# 4. Plotting the results
Y_pred = m*X + c
plt.scatter(X, Y, color='blue', label='Actual Data') 
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()