import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

data = pd.read_csv("customers.csv")
print(data.head())
data["Income"] = data[["Annual Income (k$)"]]
data["Spending"] = data[["Spending Score (1-100)"]]
data = data[["Income", "Spending"]]
print(data.head())

from sklearn.cluster import MeanShift
model = MeanShift(bandwidth=2)
model.fit(data)
pred = model.fit_predict(data)
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(12, 10))
plt.scatter(data["Income"], data["Spending"], c=pred, cmap='rainbow', alpha=0.9)
plt.show()