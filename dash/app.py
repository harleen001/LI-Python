import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html
import plotly.express as px
import pandas as pd

def load_data():
    try:
        df = pd.read_csv("healthcare.csv")
    except FileNotFoundError:
        # Dummy data for immediate testing
        df = pd.DataFrame({
            "Gender": ["Male", "Female", "Male", "Female"],
            "Age": [25, 30, 45, 50],
            "Medical Condition": ["Flu", "Cold", "Flu", "Allergy"],
            "Billing Amount": [1000, 2000, 1500, 3000],
            "Insurance Provider": ["Aetna", "Blue Cross", "Aetna", "Cigna"],
            "Date of Admission": pd.to_datetime(["2023-01-01", "2023-01-05", "2023-02-01", "2023-02-15"])
        })
    
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"], errors='coerce')
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
    df["YearMonth"] = df["Date of Admission"].dt.to_period("M").astype(str)
    return df

df = load_data()

# --- CALCULATE STATS FIRST ---
num_records = len(df)
avg_billing = f"${df['Billing Amount'].mean():,.2f}"

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    # 1. Header
    dbc.Row([
        dbc.Col([html.H1("HealthCare Dashboard", className="text-center my-4")], width=12)
    ]),

    # 2. Stats Summary (Corrected widths to 6+6=12)
    dbc.Row([
        dbc.Col([
            html.Div([
                html.B("Total Patient Records: "), html.Span(num_records)
            ], className="text-center p-3 border bg-light")
        ], width=6),
        dbc.Col([
            html.Div([
                html.B("Average Billing Amount: "), html.Span(avg_billing)
            ], className="text-center p-3 border bg-light")
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
                        placeholder="Filter by Gender",
                        clearable=True
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
                        options=[{'label': i, 'value': i} for i in df['Medical Condition'].unique()],
                        placeholder="Select Condition"
                    ),
                    dcc.Graph(id="condition-distribution")
                ])
            ])
        ], width=6), 
    ], className="mb-4"),

    # 4. Insurance Row
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                     html.H4('Insurance Provider Comparison', className="card-title"),
                     dcc.Graph(id="insurance-comparison")
                ])
            ])
        ], width=12)
    ], className="mb-4"),

    # ... (Other rows for Billing and Trends as per your previous structure)
    
], fluid=True)

# --- CALLBACKS (This is what makes it interactive!) ---

@app.callback(
    Output("age-distribution", "figure"),
    [Input("gender-filter-1", "value")]
)
def update_age_chart(selected_gender):
    filtered_df = df
    if selected_gender:
        filtered_df = df[df["Gender"] == selected_gender]
    
    fig = px.histogram(filtered_df, x="Age", nbins=20, title="Age Distribution",
                       color_discrete_sequence=['#007bff'])
    return fig

@app.callback(
    Output("condition-distribution", "figure"),
    [Input("condition-filter-2", "value")]
)
def update_condition_chart(selected_condition):
    # If a condition is selected, highlight it; otherwise show all
    fig = px.pie(df, names='Medical Condition', title="Conditions Overview", hole=0.3)
    return fig

@app.callback(
    Output("insurance-comparison", "figure"),
    Input("gender-filter-1", "value") # Just as an example trigger
)
def update_insurance_chart(val):
    fig = px.bar(df, x="Insurance Provider", y="Billing Amount", color="Medical Condition", barmode="group")
    return fig

if __name__ == "__main__":
    app.run(debug=True)