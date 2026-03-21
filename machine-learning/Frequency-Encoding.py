import pandas as pd

data = pd.Series(['Apple', 'Banana', 'Apple', 'Orange', 'Banana'])

# Compute frequency of each category
frequency = data.value_counts(normalize=True)

# Replace categories with frequencies
encoded_features = data.map(frequency)
print(encoded_features)