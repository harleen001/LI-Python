import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())


plt.pie(df['total_units'])
plt.title("bathingsoap sales data")
plt.xlabel("Month Number")
plt.ylabel("Sales unit in number")
plt.legend()
plt.show()  #printed data,
plt.savefig(fname='Bathingsoap')