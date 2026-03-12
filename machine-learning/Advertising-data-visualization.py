import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load the advertising dataset
url = 'Advertising.csv'
data = pd.read_csv(url)

# Visualize the relationship between advertising channels and sales
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].scatter(data['TV'], data['Sales'])
axs[0].set_title('TV vs. Sales')
axs[0].set_xlabel('TV Advertising Spending')
axs[0].set_ylabel('Sales')

axs[1].scatter(data['Radio'], data['Sales'])
axs[1].set_title('Radio vs. Sales')
axs[1].set_xlabel('Radio Advertising Spending')
axs[1].set_ylabel('Sales')

axs[2].scatter(data['Newspaper'], data['Sales'])
axs[2].set_title('Newspaper vs. Sales')
axs[2].set_xlabel('Newspaper Advertising Spending')
axs[2].set_ylabel('Sales')

plt.tight_layout()
plt.show()

# Split data into features (X) and target (y)
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Create and train a linear regression model
model = LinearRegression()
model.fit(X, y)

# Predict sales
predicted_sales = model.predict(X)

# Calculate and print the R-squared score
r2 = r2_score(y, predicted_sales)
print(f"R-squared: {r2:.2f}")