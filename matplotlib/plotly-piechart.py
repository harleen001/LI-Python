import plotly.express as px
import pandas as pd
df = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [40, 60, 30, 50, 20]
})

fig = px.pie(df, values='value', names='category', title='Basic Pie Chart',hole=0.8)
fig.show()   