import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

np.random.seed(0)
n_samples = 100
bedrooms = np.random.randint(1, 6, size=n_samples)
sqft = np.random.randint(1000, 3000, size=n_samples)
age = np.random.randint(1, 21, size=n_samples)
price = 50000 + 10000 * bedrooms + 200 * sqft - 1000 * age + np.random.normal(0, 5000, size=n_samples)

data = pd.DataFrame({'Bedrooms': bedrooms, 'Sqft': sqft, 'Age': age, 'Price': price})

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['Bedrooms'], data['Sqft'], data['Age'], c=data['Price'], cmap='viridis')
ax.set_xlabel('Bedrooms')
ax.set_ylabel('Sqft')
ax.set_zlabel('Age')
ax.set_title('Home Prices')
plt.show()

X = data[['Bedrooms', 'Sqft', 'Age']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)
predicted_prices = model.predict(X)
mse = mean_squared_error(y, predicted_prices)
print(f"Mean Squared Error: {mse:.2f}")