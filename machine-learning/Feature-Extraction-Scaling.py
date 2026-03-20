from sklearn.preprocessing import MinMaxScaler

data = [[10, 0.5], [20, 0.8], [15, 0.7]]

print(data)

# Create an instance of the MinMaxScaler
scaler = MinMaxScaler()

# Apply scaling to the data
scaled_features = scaler.fit_transform(data)


print(scaled_features)