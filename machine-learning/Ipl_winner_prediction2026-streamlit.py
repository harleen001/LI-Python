import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

st.set_page_config(layout="wide")
st.title("IPL 2026 Multivariate Regression Analysis")

df = pd.read_csv('ipl_winner.csv')
df['Win_Percentage'] = df['Win_Percentage'].str.replace('%', '').astype(float)

le = LabelEncoder()
all_teams = pd.concat([df['Winner'], df['Runner-up']]).unique()
le.fit(all_teams)
df['Winner_ID'] = le.transform(df['Winner'])
df['Runner_up_ID'] = le.transform(df['Runner-up'])

X = df[['Year', 'Win_Percentage']].values
y = df[['Winner_ID', 'Runner_up_ID']].values
model = LinearRegression()
model.fit(X, y)

st.sidebar.header("Prediction Inputs")
input_win_perc = st.sidebar.slider("Projected Win Percentage", 40.0, 80.0, 65.0)

test_input = np.array([[2026, input_win_perc]])
predictions = model.predict(test_input)

def get_team_name(val):
    idx = int(np.round(val))
    idx = max(0, min(idx, len(le.classes_) - 1))
    return le.inverse_transform([idx])[0]

final_winner = get_team_name(predictions[0][0])
final_runner = get_team_name(predictions[0][1])

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=df['Year'],
    y=df['Win_Percentage'],
    z=df['Winner_ID'],
    mode='markers',
    marker=dict(size=8, color=df['Winner_ID'], colorscale='Viridis', opacity=0.8),
    text=df['Winner'],
    name='Past Winners'
))

fig.add_trace(go.Scatter3d(
    x=[2026],
    y=[input_win_perc],
    z=[predictions[0][0]],
    mode='markers',
    marker=dict(size=12, color='red', symbol='diamond'),
    name='2026 Prediction',
    text=[f"Predicted: {final_winner}"]
))

fig.update_layout(
    scene=dict(
        xaxis_title='Year',
        yaxis_title='Win %',
        zaxis_title='Winner Team (LE)'
    ),
    margin=dict(l=0, r=0, b=0, t=40),
    title=f"Prediction: {final_winner} (Winner) vs {final_runner} (Runner-up)",
    template="plotly_dark"
)

st.plotly_chart(fig, use_container_width=True)