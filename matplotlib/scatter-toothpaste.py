import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())
x=df['month_number']

plt.scatter(x,df['toothpaste'], label='Toothpaste Sales Data')


plt.xlabel("Month Number")
plt.ylabel("Number of units sold")
plt.legend(loc='upper left') 
plt.grid()
plt.show()  #printed data,