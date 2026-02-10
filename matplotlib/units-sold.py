import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("company_sales_data.csv")
print(df.head())
x=df['month_number']
y=df['total_units']

facecream =plt.plot(x,df['facecream'],color='blue',linewidth=3,label='Face Cream Sales Data')
plt.scatter(x,df['facecream'],color='blue')

facewash=plt.plot(x,df['facewash'],color='orange',linewidth=3,label='Face Wash Sales Data')
plt.scatter(x,df['facewash'],color='orange')

toothpaste=plt.plot(x,df['toothpaste'],color='green',linewidth=3,label='Toothpaste Sales Data')
plt.scatter(x,df['toothpaste'],color='green')

bathingsoap=plt.plot(x,df['bathingsoap'],color='red',linewidth=3,label='Bathing Soap Sales Data')
plt.scatter(x,df['bathingsoap'],color='red')

shampoo=plt.plot(x,df['shampoo'],color='brown',linewidth=3,label='Shampoo Sales Data')
plt.scatter(x,df['shampoo'],color='brown')

plt.xlabel("Month Number")
plt.ylabel("Sales units in numbers")
plt.legend(loc='upper left') 
plt.show()  #printed data,