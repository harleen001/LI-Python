import dash
import dash_bootstrap_components as dbc
from dash import dcc, Input, Output, html #dash core components       
import plotly.express as px    # for charts 
import pandas as pd

def load_data():
    df=pd.read_csv("healthcare.csv")
    df["Billing Amount"] = pd.to_numeric(df["Billing Amount"],errors='coerce')  #treats any error as NAN
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
    df["YearMonth"]=df["Date of Admission"].dt.to_period("M")   #to Months
    return df


data=load_data()


#creating a web app
app=dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])  #bootstrap components

app.layout = dbc.Container(      

#dbc is a class which has container
dbc.Row([
    dbc.Col([html.H1("HealthCare Dashboard")], width=15,className="text-center my-5")
])

#Hospital statistics row

)



if __name__=="__main__":
    app.run(debug=True)