import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset with 2 targets (Price and Days_on_Market)
data = pd.DataFrame({
    'Size': [1200, 1500, 1700, 900, 1100],
    'Bedrooms': [3, 3, 2, 2, 1],
    'Crime_Rate': [0.05, 0.02, 0.07, 0.01, 0.04],
    # Targets (Y)
    'Price': [220000, 300000, 280000, 150000, 180000],
    'Days_on_Market': [45, 20, 50, 15, 30]
})

# X: Features (Independent)
X = data[['Size', 'Bedrooms', 'Crime_Rate']]

# y: Targets (Dependent) - Note we pass a LIST of columns
y = data[['Price', 'Days_on_Market']]


model = LinearRegression()
model.fit(X, y)

new_house = np.array([[1400, 3, 0.03]])
predictions = model.predict(new_house)

price_pred = predictions[0][0]
days_pred = predictions[0][1]

print(f"Predicted Price: ${price_pred:,.2f}")
print(f"Predicted Days on Market: {int(days_pred)} days")