import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

st.set_page_config(layout="wide")
st.title("Interactive Cricket Prediction")
balls_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]).reshape(-1, 1)
scores_train = np.array([1, 2, 6, 4, 2, 6, 1, 1, 2, 4, 4, 6]) 
model = LinearRegression().fit(balls_train, scores_train)

col1, col2 = st.columns(2)

with col1:
    st.header("Actual Data")
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=balls_train.flatten(), y=scores_train, mode='markers', name='Actual'))
    x_line = np.array([1, 12]).reshape(-1, 1)
    y_line = model.predict(x_line)
    fig1.add_trace(go.Scatter(x=x_line.flatten(), y=y_line, mode='lines', name='Best Fit', line=dict(color='gray', dash='dash')))
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.header("Predictive Analysis")
    input_str = st.text_input("Enter balls:", "10, 20, 30, 50") 
    vals = sorted([float(x.strip()) for x in input_str.split(',')])
    test_balls = np.array(vals).reshape(-1, 1)
    predicted_scores = model.predict(test_balls).astype(int)
    
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=vals, y=predicted_scores, mode='markers+text', 
                              text=predicted_scores, textposition="top center",
                              marker=dict(size=12, color='green'), name='Predictions'))
    x_range = np.array([min(vals), max(vals)]).reshape(-1, 1)
    y_range = model.predict(x_range)
    fig2.add_trace(go.Scatter(x=x_range.flatten(), y=y_range, mode='lines', 
                              line=dict(color='red'), name='Best Fit Line'))
    st.plotly_chart(fig2, use_container_width=True)