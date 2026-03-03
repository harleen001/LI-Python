import pandas as pd
import plotly.express as px

df = pd.read_csv("employee.csv")
df.columns = df.columns.str.strip() 

col_job = 'Job'
col_ename = 'Ename'
col_salary = 'Salary'
col_dept = 'DeptNo'

fig = px.bar(
    df, x=col_ename, y=col_salary, color=col_dept,hover_data=['Empid', 'Comm', col_job],
    template="plotly_white"
)

jobs = sorted(df[col_job].unique())
buttons = []

buttons.append(dict(
    method="restyle",label="All Jobs",
    args=[{"x": [df[col_ename]], "y": [df[col_salary]], "marker.color": [df[col_dept]]}]
))

for job in jobs:
    filtered = df[df[col_job] == job]
    buttons.append(dict(
        method="restyle",label=job,
        args=[{"x": [filtered[col_ename]], "y": [filtered[col_salary]],"marker.color": [filtered[col_dept]]  }]
    ))

fig.update_layout(
    updatemenus=[{
        "buttons": buttons,"direction": "down","showactive": True,
        "x": 0.0,"y": 1.15,"xanchor": "left","yanchor": "top"
    }],
    margin=dict(t=100)
)
fig.show()