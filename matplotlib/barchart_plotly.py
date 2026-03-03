import plotly.express as px
import numpy as np
x=np.array([10,20,30,40])
y=np.array(['a','b','c','d'])

abc=px.bar(x,y)
abc.show()