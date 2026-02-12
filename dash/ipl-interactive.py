from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df_player = pd.read_csv("batsman.csv")
df_match = pd.read_csv("match.csv")

df_merged = pd.merge(df_player, df_match, left_on='match_no', right_on='match_number', how='left')
df_merged['batting_team'] = df_merged.apply(lambda row: row['team1'] if row['inningno'] == 1 else row['team2'], axis=1)

COLORS = ["#2c3e50", "#34495e", "#5dade2", "#aed6f1", "#16a085", "#1abc9c"]

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY]) # Professional, soft gray/white theme

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("IPL Performance Analytics", 
                        className="text-center mb-4 mt-4", 
                        style={'color': '#2c3e50', 'fontWeight': 'bold'}), width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            html.Label("Tournament Stage:", style={'color': '#2c3e50'}),
                            dcc.Dropdown(
                                id='match-stage-filter',
                                options=[{'label': i, 'value': i} for i in df_match['match_type'].unique()],
                                multi=True,
                                placeholder="Select Stages"
                            )
                        ], md=4),
                        dbc.Col([
                            html.Label("Minimum Runs:", style={'color': '#2c3e50'}),
                            dcc.Input(id='run-threshold', type='number', value=100, className="form-control")
                        ], md=4),
                        dbc.Col([
                            html.Label("Venue Selection:", style={'color': '#2c3e50'}),
                            dcc.Dropdown(
                                id='venue-filter',
                                options=[{'label': i, 'value': i} for i in df_match['venue'].unique()],
                                placeholder="Select Venue"
                            )
                        ], md=4),
                    ])
                ])
            ], className="mb-4 border-0 shadow-sm", style={'backgroundColor': '#f8f9fa'})
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Player Scoring Contribution", className="bg-white border-0", style={'color': '#2c3e50', 'fontWeight': 'bold'}),
                dbc.CardBody([dcc.Graph(id='player-pie-chart')])
            ], className="shadow-sm border-0")
        ], md=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Team Runs by Match Type", className="bg-white border-0", style={'color': '#2c3e50', 'fontWeight': 'bold'}),
                dbc.CardBody([dcc.Graph(id='team-stage-bar')])
            ], className="shadow-sm border-0")
        ], md=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Workload Analysis: Balls Faced vs. Total Score", className="bg-white border-0", style={'color': '#2c3e50', 'fontWeight': 'bold'}),
                dbc.CardBody([dcc.Graph(id='consistency-scatter')])
            ], className="shadow-sm border-0")
        ], md=12)
    ])
], fluid=True)


@app.callback(
    [Output('player-pie-chart', 'figure'),
     Output('team-stage-bar', 'figure'),
     Output('consistency-scatter', 'figure')],
    [Input('match-stage-filter', 'value'),
     Input('run-threshold', 'value'),
     Input('venue-filter', 'value')]
)
def update_dashboard(stages, threshold, venue):
    dff = df_merged.copy()
    if stages:
        dff = dff[dff['match_type'].isin(stages)]
    if venue:
        dff = dff[dff['venue'] == venue]
    
    #Pie Chart
    player_runs = dff.groupby('batter')['score'].sum().reset_index()
    player_runs = player_runs[player_runs['score'] >= (threshold or 0)].sort_values(by='score', ascending=False)
    
    fig_pie = px.pie(
        player_runs.head(15), 
        values='score', names='batter',
        hole=0.4, template="plotly_white",
        color_discrete_sequence=px.colors.sequential.Blues_r
    )
    fig_pie.update_layout(margin=dict(t=30, b=10, l=10, r=10))

    #Bar Chart
    team_stage = dff.groupby(['batting_team', 'match_type'])['score'].sum().reset_index()
    fig_bar = px.bar(
        team_stage, x='match_type', y='score', color='batting_team',
        barmode='group', template="plotly_white",
        color_discrete_sequence=px.colors.qualitative.Safe 
    )

    #scatter plot
    player_stats = dff.groupby('batter').agg(
        total_runs=('score', 'sum'),
        balls_faced=('batter', 'count')
    ).reset_index()
    player_stats = player_stats[player_stats['total_runs'] >= (threshold or 50)]

    fig_scatter = px.scatter(
        player_stats, x='balls_faced', y='total_runs',
        hover_name='batter', size='total_runs', 
        color='total_runs', color_continuous_scale='GnBu', 
        template="plotly_white"
    )
    fig_scatter.update_layout(coloraxis_showscale=False)

    return fig_pie, fig_bar, fig_scatter

if __name__ == '__main__':
    app.run(debug=True)