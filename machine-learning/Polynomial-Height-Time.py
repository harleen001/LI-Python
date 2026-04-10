import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("Height vs Time")

# Data: Time in seconds, Height in meters
time = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3])
height = np.array([0, 11, 18, 21, 20, 15, 6])


weights = np.polyfit(time, height, 2)
model = np.poly1d(weights)

t_range = np.linspace(0, 3, 100)
h_pred = model(t_range)

fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=height, mode='markers', name='Observed'))
fig.add_trace(go.Scatter(x=t_range, y=h_pred, mode='lines', name='Trajectory', line=dict(dash='dash')))
fig.update_layout(xaxis_title="Time (s)", yaxis_title="Height (m)")

st.plotly_chart(fig)