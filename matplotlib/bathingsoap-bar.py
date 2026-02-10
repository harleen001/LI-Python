import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())
x=df['month_number']

plt.bar(x,df['bathingsoap'],color='blue')

plt.title("bathingsoap sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales unit in number")
plt.grid()
plt.show()  #printed data,
plt.savefig(fname='Bathingsoap')