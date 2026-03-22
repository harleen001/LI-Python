import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Response': [1.2, 1.5, 3.8, 3.6, 5.1]  })
# Reshape data if necessary
data['Response'] = np.array([1.2, 1.5, 3.8, 3.6, 5.1])
kmeans = KMeans(n_clusters=2, random_state=0)
data['Cluster'] = kmeans.fit_predict(data[['Response']])
print(data)