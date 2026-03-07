import dash
from dash import dcc, html, Input, Output
import pandas as pd

states_df = pd.read_csv('merged_population_data.csv')
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Dropdown(
        id='state-dropdown',
        options=[{'label': state, 'value': state} for state in states_df['State.Name'].unique()],
        placeholder="Select a state"
    ),
    dcc.Graph(id='india-map')
])

@app.callback(
    Output('india-map', 'figure'),
    Input('state-dropdown', 'value')
)
def update_map(selected_state):
    colors = ['green' if state == selected_state else 'blue' for state in states_df['State.Name']]

    marker_data = {
        'type': 'scattermapbox',
        'lat': states_df['latitude'],
        'lon': states_df['longitude'],
        'mode': 'markers',
        'marker': {
            'size': 12,
            'color': colors
        },
        'text': states_df['State.Name'],
        'hovertemplate': (
            '<b>%{text}</b><br>' +
            'Population: %{customdata[0]:,}<extra></extra>'
        ),
        'customdata': states_df[['total_population']].values,
        'name': 'States'
    }

    layout = {
        'mapbox': {
            'style': 'open-street-map',
            'center': {'lat': 20.5937, 'lon': 78.9629},
            'zoom': 3
        },
        'margin': {'l': 0, 'r': 0, 't': 0, 'b': 0}
    }

    return {'data': [marker_data], 'layout': layout}

if __name__ == '__main__':
    app.run(debug=True)
