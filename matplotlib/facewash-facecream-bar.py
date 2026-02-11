import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())
x=df['month_number']

plt.bar(x,df['facecream'], label='Facecream Sales Data',width=0.5,color='blue')
plt.bar(x,df['facewash'], label='Facewash Sales Data',width=0.1,color='orange')


plt.xlabel("Month Number")
plt.ylabel("Number of units sold")
plt.legend(loc='upper left') 
plt.grid()
plt.show()  #printed data,