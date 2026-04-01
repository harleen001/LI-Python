import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("ad_spend_sales.csv")

X = df[['Ad_Spend']] 
y = df['Sales']


trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(trainX, trainY)


Y_pred = model.predict(testX)

accuracy = model.score(testX, testY)

newx=np.array([[3.5]])
Y_pred_new=model.predict(newx)


print(f"R-squared Score: {accuracy:.4f}")

plt.scatter(X,y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line') 
plt.xlabel('Ad Spend')
plt.ylabel('Sales')
plt.legend()
plt.show()