import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())


plt.hist(df['total_profit'])
plt.title("bathingsoap sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales unit in number")
plt.grid()
plt.show()  #printed data,
plt.savefig(fname='Bathingsoap')