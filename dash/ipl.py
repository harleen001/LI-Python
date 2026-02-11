from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

# --- 1. DATA PREPARATION ---
df_player = pd.read_csv("batsman.csv")
df_match = pd.read_csv("match.csv")

# Logic for Pie Chart (Individual Batsmen)
batsman_runs = df_player.groupby('batter')['score'].sum().reset_index()
batsman_runs = batsman_runs.sort_values(by='score', ascending=False)
batsman_filtered = batsman_runs[batsman_runs['score'] >= 500]

# Logic for Bar Chart (Team Runs)
df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')
df_merged['batting_team'] = df_merged.apply(
    lambda row: row['team1'] if row['inningno'] == 1 else row['team2'], axis=1
)
team_runs = df_merged.groupby('batting_team')['score'].sum().reset_index().sort_values(by='score', ascending=False)
top_teams = team_runs.head(5)

# --- 2. CREATE PLOTLY FIGURES ---
# Pie Chart using Plotly Express
fig_pie = px.pie(
    batsman_filtered, 
    values='score', 
    names='batter', 
    title='Individual Scores (>= 500)',
    hole=0.3  # Optional: makes it a donut chart
)
# This line ensures the actual score is shown on the slice
fig_pie.update_traces(textinfo='value+label')

# Bar Chart using Plotly Express
fig_bar = px.bar(
    top_teams, 
    x='batting_team', 
    y='score', 
    title='Top 5 Teams by Total Runs',
    text='score',
    color='score'
)
fig_bar.update_traces(textposition='outside')

# --- 3. DASH LAYOUT ---
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Cricket Analytics Dashboard", style={'textAlign': 'center', 'fontFamily': 'Arial'}),
    
    html.Div([
        html.Div([
            dcc.Graph(id='pie-graph', figure=fig_pie)
        ], style={'width': '48%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='bar-graph', figure=fig_bar)
        ], style={'width': '48%', 'display': 'inline-block'})
    ])
])

if __name__ == '__main__':
    app.run(debug=True)