from sklearn.preprocessing import MinMaxScaler
import numpy as np

# Sample data
data = np.array([[10], [20], [30], [40], [50]])

# Initialize the MinMaxScaler
scaler = MinMaxScaler()

# Fit the scaler to the data and transform it
normalized_data = scaler.fit_transform(data)

print("Original Data:")
print(data)
print("\nNormalized Data (Min-Max Scaled):")
print(normalized_data)