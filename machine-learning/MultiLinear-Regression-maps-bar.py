import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_california_housing

# 1. Load and preprocess data (using California Housing dataset as example)
housing = fetch_california_housing()
housing_df = pd.DataFrame(housing.data, columns=housing.feature_names)
housing_df['MedHouseValue'] = housing.target
selected_features = ['MedInc', 'AveRooms', 'AveOccup', 'HouseAge']
X = housing_df[selected_features]
y = housing_df['MedHouseValue']

# Standardize features for comparable coefficients
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Fit the Linear Regression model
model = LinearRegression()
model.fit(X_scaled, y)

# 3. Get feature coefficients and create a DataFrame
feature_importance = pd.DataFrame({'Feature': selected_features, 'Coefficient': model.coef_})
feature_importance['Absolute_Coefficient'] = abs(feature_importance['Coefficient'])
feature_importance = feature_importance.sort_values(by='Absolute_Coefficient', ascending=False)

# 4. Visualize feature importance using a bar chart
plt.figure(figsize=(10, 6))
plt.bar(feature_importance['Feature'], feature_importance['Coefficient'], color=['blue' if c > 0 else 'red' for c in feature_importance['Coefficient']])
plt.xlabel('Features')
plt.ylabel('Coefficient Value (Standardized)')
plt.title('Feature Importance in Multiple Linear Regression Model')
plt.xticks(rotation=45)
plt.show()
