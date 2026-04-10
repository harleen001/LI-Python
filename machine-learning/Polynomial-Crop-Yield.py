import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

st.title("Fertilizer Optimization")
st.write("Find the crop yield using Polynomial Regression.")

# Dataset: Fertilizer (kg/hectare) vs. Crop Yield (tonnes/hectare)
# Yield increases, peaks, then drops due to over-fertilization
X = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160]).reshape(-1, 1)
y = np.array([2.1, 3.5, 4.8, 5.2, 5.5, 5.3, 4.7, 3.8, 2.5]).reshape(-1, 1)


degree = st.sidebar.select_slider("Model Sensitivity (Degree)", options=[1, 2, 3, 4], value=2)

poly_features = PolynomialFeatures(degree=degree)
X_poly = poly_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

X_new = np.linspace(0, 180, 100).reshape(-1, 1)
X_new_poly = poly_features.transform(X_new)
y_new = model.predict(X_new_poly)

fig = go.Figure()
fig.add_trace(go.Scatter(x=X.flatten(), y=y.flatten(), mode='markers', name='Field Data',marker=dict(size=12, color='forestgreen')))
fig.add_trace(go.Scatter(x=X_new.flatten(), y=y_new.flatten(), mode='lines', name='Yield Prediction',line=dict(color='orange', width=4)))
fig.update_layout(xaxis_title="Fertilizer Used (kg/hectare)",yaxis_title="Crop Yield (tonnes/hectare)",template="plotly_dark",hovermode="x unified")

st.plotly_chart(fig, use_container_width=True)

max_idx = np.argmax(y_new)
best_fert = X_new[max_idx][0]
best_yield = y_new[max_idx][0]

st.success(f"To maximize yield, use approximately {best_fert:.1f} kg of fertilizer to get {best_yield:.2f} per hectare.")