from sklearn.preprocessing import LabelEncoder

data = ['Low', 'High', 'Medium', 'Low']

 # Create an instance of the LabelEncoder
encoder = LabelEncoder()

 # Apply label encoding
encoded_features = encoder.fit_transform(data)
print(encoded_features)
