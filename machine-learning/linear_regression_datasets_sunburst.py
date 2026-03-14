import pandas as pd
import plotly.express as px
from CustomLinearRegression import MyLinearRegression
from CustomR import get_accuracy
import numpy as np

df = pd.read_csv("Pepsi.csv")
model = MyLinearRegression()

x = df['Year'].values 
y = df['Actual_Price'].values
model.fit(x, y)

future_years = np.array([2026, 2027, 2028, 2029, 2030])
all_years = np.concatenate([x, future_years])
all_preds = model.predict(all_years)

plot_df = pd.DataFrame({'Year': all_years,'Actual': np.concatenate([y, [np.nan] * 5]),'Predicted': all_preds})

melted_df = plot_df.melt(id_vars=['Year'], value_vars=['Actual', 'Predicted'], var_name='Type', value_name='Price')
melted_df = melted_df.dropna(subset=['Price'])

fig = px.sunburst(melted_df, path=['Year', 'Type'], values='Price',title="Pepsi Price Structure: Year > Type",
    color='Type')

fig.update_layout(template="plotly_white")
fig.show()
