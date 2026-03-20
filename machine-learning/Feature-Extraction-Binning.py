import numpy as np

data = [2.5, 3.7, 1.9, 4.2, 5.1, 2.8]

print(data)

# Create four bins from 1 to 6
bins = np.linspace(1, 6, 4)

# Assign each value to a bin
binned_features = np.digitize(data, bins)
print(binned_features)
