import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px
import pandas as pd

def load_data():
    # Using a dummy dict for demonstration if file is missing
    try:
        df = pd.read_csv("healthcare.csv")
    except FileNotFoundError:
        return pd.DataFrame() 
        
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors='coerce')
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
    # Convert to string because Plotly doesn't always play nice with Period objects
    df["YearMonth"] = df["Date of Admission"].dt.to_period("M").astype(str)
    return df

df = load_data()

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # Header Row
    dbc.Row([
        dbc.Col([html.H1("HealthCare Dashboard")], width=12, className="text-center my-4")
    ]),

    # Hospital statistics row
    dbc.Row([
        # First Column (Patient Demographics)
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Patient Demographics', className="card-title"),
                    dcc.Dropdown(
                        id="gender-filter-1", 
                        options=[{'label': i, 'value': i} for i in df['Gender'].unique()] if not df.empty else [],
                        placeholder="Select Gender"
                    ),
                    dcc.Graph(id="age-distribution")
                ])
            ])
        ], width=6), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Medical Condition Distribution', className="card-title"),
                    dcc.Dropdown(
                        id="condition-filter-2", 
                        options=[{'label': i, 'value': i} for i in df['Medical Condition'].unique()] if not df.empty else [],
                        placeholder="Select Condition"
                    ),
                    dcc.Graph(id="condition-distribution")
                ])
            ])
        ], width=6), 
    ]),
], fluid=True)

#Insurance data provider

if __name__ == "__main__":
    app.run(debug=True)