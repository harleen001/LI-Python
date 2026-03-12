import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.DataFrame({
    'Size': [1200, 1500, 1700, 900, 1100],
    'Bedrooms': [3, 3, 2, 2, 1],
    'Crime_Rate': [0.05, 0.02, 0.07, 0.01, 0.04],
    'Price': [220000, 300000, 280000, 150000, 180000]
})

X = data[['Size', 'Bedrooms', 'Crime_Rate']]
y = data['Price']

model = LinearRegression()
model.fit(X, y)
new_house = np.array([[1400, 2, 0.03]])
predicted_price = model.predict(new_house)

print(f"Predicted price of the new house: ${predicted_price[0]:,.2f}")