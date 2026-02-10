import matplotlib.pyplot as plt
import pandas as pd

x=[1,2,3]
y=[4,5,6]
#plt.plot(x,y)
#plt.grid()  #to get grid
#plt.show()   #simple plot


#PyPlot API 
#Univariate (single data) - Numerical
Data={
    "Salary": [25000,30000,70000,45000,32000,61000,29000,38000,31000,45000]
}
df=pd.DataFrame(Data)

#LINE PLOT
plt.plot(df['Salary'],color="red",marker='o',linestyle="--",linewidth=2)  #marks data as o round, linestyle can be -- : etc.
plt.grid()
plt.show()