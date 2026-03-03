import plotly.express as px
import numpy as np
xvalues=np.array([10,20,30,40,50,60,70,80,90,100])
yvalues=np.array([10,20,30,40,50,60,70,80,90,100])

fig = px.scatter(x=xvalues,y=yvalues)
fig.show()   