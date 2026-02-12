import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px
import pandas as pd

def load_data():
    try:
        df = pd.read_csv("healthcare.csv")
    except FileNotFoundError:
        # Dummy data for demonstration
        df = pd.DataFrame({
            "Gender": ["Male", "Female", "Male", "Female", "Male"],
            "Age": [25, 30, 45, 50, 35],
            "Medical Condition": ["Flu", "Cold", "Flu", "Allergy", "Cold"],
            "Billing Amount": [1000, 15000, 8000, 25000, 5000],
            "Insurance Provider": ["Aetna", "Blue Cross", "Aetna", "Cigna", "Blue Cross"],
            "Date of Admission": pd.to_datetime(["2023-01-01", "2023-01-05", "2023-02-01", "2023-02-15", "2023-03-01"])
        })
    
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors='coerce')
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
    df["YearMonth"] = df["Date of Admission"].dt.to_period("M").astype(str)
    return df

df = load_data()
num_records = len(df)
avg_billing = f"${df['Billing Amount'].mean():,.2f}"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # 1. Header
    dbc.Row([
        dbc.Col([html.H1("HealthCare Dashboard", className="text-center my-4")], width=12)
    ]),

    # 2. Stats Summary
    dbc.Row([
        dbc.Col([
            html.Div([html.B("Total Patient Records: "), html.Span(num_records)], className="text-center p-3 border bg-light")
        ], width=6),
        dbc.Col([
            html.Div([html.B("Average Billing Amount: "), html.Span(avg_billing)], className="text-center p-3 border bg-light")
        ], width=6),
    ], className="mb-4"),

    # 3. Demographics & Conditions Row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Patient Demographics', className="card-title"),
                    dcc.Dropdown(
                        id="gender-filter-1", 
                        options=[{'label': i, 'value': i} for i in df['Gender'].unique()],
                        placeholder="Filter by Gender", clearable=True
                    ),
                    dcc.Graph(id="age-distribution")
                ])
            ])
        ], width=6), 

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Condition Distribution', className="card-title"),
                    dcc.Dropdown(
                        id="condition-filter-2", 
                        options=[{'label': i, 'value': i} for i in df['Medical Condition'].unique()],
                        placeholder="Select Condition", clearable=True
                    ),
                    dcc.Graph(id="condition-distribution")
                ])
            ])
        ], width=6), 
    ], className="mb-4"),

    # 4. Insurance & Billing Row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Billing Amount Distribution', className="card-title"),
                    dcc.Slider(
                        id="billing-slider",
                        min=0,
                        max=df["Billing Amount"].max(),
                        value=df["Billing Amount"].max(),
                        marks={i: f'${i/1000}k' for i in range(0, int(df["Billing Amount"].max())+1, 10000)},
                        step=1000
                    ),
                    dcc.Graph(id="billing-distribution")
                ])
            ])
        ], width=12)
    ], className="mb-4"),

    # 5. Trends Row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Trends in Admissions', className="card-title"),
                    dcc.RadioItems(
                        id='chart-type',
                        options=[{'label': ' Line ', 'value': 'line'}, {'label': ' Bar ', 'value': 'bar'}],
                        value='line', inline=True, className="mb-2"
                    ),
                    dcc.Dropdown(
                        id='condition-filter-trend',
                        options=[{'label': i, 'value': i} for i in df['Medical Condition'].unique()],
                        placeholder="Filter by Medical Condition", clearable=True
                    ),
                    dcc.Graph(id='admission-trends')
                ])
            ])
        ], width=12)
    ], className="mb-4")
], fluid=True)

# --- CALLBACKS ---

@app.callback(
    Output("age-distribution", "figure"),
    Input("gender-filter-1", "value")
)
def update_age(gender):
    dff = df if not gender else df[df["Gender"] == gender]
    return px.histogram(dff, x="Age", title="Age Breakdown")

@app.callback(
    Output("condition-distribution", "figure"),
    Input("condition-filter-2", "value")
)
def update_condition(selected_cond):
    pull_values = [0.2 if c == selected_cond else 0 for c in df['Medical Condition'].unique()]
    
    fig = px.pie(
        df, 
        names="Medical Condition", 
        hole=0.3,
        title="Condition Overview (Total Market Share)"
    )

    fig.update_traces(pull=pull_values)
    
    return fig

@app.callback(
    Output("billing-distribution", "figure"),
    Input("billing-slider", "value")
)
def update_billing(max_val):
    dff = df[df["Billing Amount"] <= max_val]
    return px.histogram(dff, x="Billing Amount", title=f"Bills up to ${max_val:,.0f}")

@app.callback(
    Output("admission-trends", "figure"),
    [Input("chart-type", "value"), Input("condition-filter-trend", "value")]
)
def update_trends(chart_type, cond):
    dff = df if not cond else df[df["Medical Condition"] == cond]
    trend_data = dff.groupby("YearMonth").size().reset_index(name="Admissions")
    
    if chart_type == 'line':
        return px.line(trend_data, x="YearMonth", y="Admissions", markers=True)
    return px.bar(trend_data, x="YearMonth", y="Admissions")

if __name__ == "__main__":
    app.run(debug=True)