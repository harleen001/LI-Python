import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())

x=df['month_number']
y=df['total_profit']
plt.plot(x,y, linestyle='dotted',color='red',label='Profit data of last year')
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.scatter(x,y,linewidths=3,color='black'  )
plt.legend(loc='lower right') 
plt.show()  #printed data,