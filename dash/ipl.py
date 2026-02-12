from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df_player = pd.read_csv("batsman.csv")
df_match = pd.read_csv("match.csv")


batsman_runs = df_player.groupby('batter')['score'].sum().reset_index()
batsman_runs = batsman_runs.sort_values(by='score', ascending=False)
batsman_filtered = batsman_runs[batsman_runs['score'] >= 500]


df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')
df_merged['batting_team'] = df_merged.apply(lambda row: row['team1'] if row['inningno'] == 1 else row['team2'], axis=1)
team_runs = df_merged.groupby('batting_team')['score'].sum().reset_index().sort_values(by='score', ascending=False)
top_teams = team_runs.head(5)

fig_pie = px.pie(
    batsman_filtered, values='score', names='batter',title='Top Individual Run Scorers', hole=0.4,template="plotly_white")
fig_pie.update_traces(textinfo='value+label')

fig_bar = px.bar(top_teams, x='batting_team', y='score', title='Top 5 Teams by Total Runs', text='score',color='score', 
                 color_continuous_scale='Viridis',template="plotly_white")

app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = dbc.Container([
    dbc.Row([dbc.Col(html.H1("Cricket Analytics Pro Dashboard", className="text-center text-primary mb-4 mt-4"), width=12)]),

    dbc.Row([dbc.Col([dbc.Card([dbc.CardHeader("Batsman Performance (500+ Runs)"),dbc.CardBody([dcc.Graph(figure=fig_pie)])], 
                               className="shadow") ], xs=12, md=6),
            dbc.Col([dbc.Card([dbc.CardHeader("Team Dominance"),dbc.CardBody([dcc.Graph(figure=fig_bar)])], className="shadow") ], 
                    xs=12, md=6)], className="mb-4"),], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)