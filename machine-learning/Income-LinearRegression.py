import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

data=pd.read_csv("Income.csv")
model = LinearRegression()
x=data['Income'].values.reshape(-1, 1)
y= data['Expenditure on petrol']
model.fit(x,y)
Prediction = model.predict(x)

plt.scatter(x,y, label="Expenditure on petrol")  # Data points
plt.plot(x, Prediction, color='Green', linestyle='--', label="Regression Line")  # Best fit line
plt.xlabel("Income")
plt.ylabel("Expenditure on petrol")
plt.title("Income vs Expenditure on petrol with Regression Line")
plt.legend()
plt.show()

fig = px.scatter(data, x='Income', y='Expenditure on petrol', title='Income vs Expenditure on petrol with Regression Line')
fig.add_trace(px.line(x=data['Income'], y=Prediction, title='Regression Line').data[0])
fig.update_layout(showlegend=True)
fig.show()
