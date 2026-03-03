import plotly.express as px
import numpy as np
data = np.array([
    [10, 20, 30],
    [25, 15, 35],
    [40, 22, 18]
])

fig = px.imshow(data, 
                title="Simple Heatmap",
                labels=dict(x="Columns", y="Rows", color="Value"))

fig.show()