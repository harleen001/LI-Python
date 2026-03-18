from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np

X = np.array([[2, 900], [3, 1200], [4, 1500], [5, 1800], [6, 2200]])  # Features
y = np.array([50, 75, 90, 120, 150])  # Prices

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Regression Model
regressor = RandomForestRegressor(n_estimators=10, random_state=42)  # 10 trees
regressor.fit(X_train, y_train)

# Predict house price for a house with 4 rooms and 1400 sq ft area
predicted_price = regressor.predict([[4, 1400]])
print(f"Predicted House Price: {predicted_price[0]:.2f} lakhs")