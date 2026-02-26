'''
import pandas as pd
import matplotlib.pyplot as plt

d={'Pid':pd.Series([1,2,3,4,5,6,7]),
   'Pname':pd.Series(['Rin','Lux','Pepsi','Eraser','Pen','Pencil','Register']),
   'Prate':pd.Series([85,90,35,30,96,20,150])}

df=pd.DataFrame(d)
plt.plot(df['Pname'],df['Prate'])
for x,y in zip(df['Pname'],df['Prate']):
    plt.text(x,y+5,y)   # x and y location and coordinate to show location
plt.show()
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

d={'Pid':pd.Series([1,2,3,4,5,6,7]),
   'Pname':pd.Series(['Rin','Lux','Pepsi','Eraser','Pen','Pencil','Register']),
   'Prate':pd.Series([85,90,35,30,96,20,150])}

df=pd.DataFrame(d)
plt.plot(df['Pname'],df['Prate'])
for x,y in zip(df['Pname'],df['Prate']):
    plt.text(x,y+5,y)   # x and y location and coordinate to show location
st.pyplot(plt)


fig = px.line(df, x=df["Pname"], y=df["Prate"], title='Product Information',text=df["Prate"])
st.plotly_chart(fig)