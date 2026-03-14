import pandas as pd
import matplotlib.pyplot as plt
# Import your custom class from the file you just created
from CustomLinearRegression import MyLinearRegression 

data = pd.read_csv("Income.csv")

# Use your custom model instead of sklearn
model = MyLinearRegression()

x = data['Income'].values
y = data['Expenditure on petrol'].values

# The process remains the same!
model.fit(x, y)
Prediction = model.predict(x)

# Visualization code...
plt.scatter(x, y, label="Actual Data")
plt.plot(x, Prediction, color='Green', linestyle='--', label="Manual Regression Line")
plt.show()

print(f"Calculated Slope: {model.slope}")
print(f"Calculated Intercept: {model.intercept}")