from sklearn.preprocessing import OneHotEncoder

data = [['Red'], ['Blue'], ['Green'], ['Red']]

# Create an instance of the OneHotEncoder
encoder = OneHotEncoder()

# Apply one-hot encoding
onehot_features = encoder.fit_transform(data).toarray()
print(onehot_features)
