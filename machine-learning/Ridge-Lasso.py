import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import Ridge, Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import plotly.graph_objects as go
import numpy as np

# Prepare data
X = np.array([10,21 ,45 ,56 ,78 ,70 ,44 ,55 ,65 ,67 ]).reshape(-1, 1)
y = np.array([5,1 ,4 ,6 ,8 ,7 ,4 ,25 ,26 ,16 ])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ridge Regression
ridge_model = Ridge(alpha=1.0)
ridge_model.fit(X_train, y_train)
ridge_pred = ridge_model.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_pred)
print("Ridge Mean Squared Error:", ridge_mse)

# Lasso Regression
lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, y_train)
lasso_pred = lasso_model.predict(X_test)
lasso_mse = mean_squared_error(y_test, lasso_pred)
print("Lasso Mean Squared Error:", lasso_mse)



data = fetch_california_housing()
X = data.data
y = data.target
feature_names = data.feature_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(X_train_scaled, y_train)
lasso.fit(X_train_scaled, y_train)

ridge_coef = ridge.coef_
lasso_coef = lasso.coef_

df = pd.DataFrame({
    'Feature': feature_names,
    'Ridge Coefficient': ridge_coef,
    'Lasso Coefficient': lasso_coef
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['Feature'],
    y=df['Ridge Coefficient'],
    name='Ridge Coefficient',
    marker_color='blue',
    text=df['Ridge Coefficient'].round(3),
    textposition='auto',
    hovertemplate='Feature: %{x}<br>Ridge Coef: %{y:.4f}<extra></extra>'
))

fig.add_trace(go.Bar(
    x=df['Feature'],
    y=df['Lasso Coefficient'],
    name='Lasso Coefficient',
    marker_color='red',
    text=df['Lasso Coefficient'].round(3),
    textposition='auto',
    hovertemplate='Feature: %{x}<br>Lasso Coef: %{y:.4f}<extra></extra>'
))

fig.update_layout(
    title='Interactive Comparison of Ridge and Lasso Regression Coefficients',
    xaxis_title='Features',
    yaxis_title='Coefficient Value',
    barmode='group',
    template='plotly_dark',
    legend=dict(x=0.7, y=1.1, bgcolor='rgba(0,0,0,0)'),
    hovermode='x unified'
)

fig.show()