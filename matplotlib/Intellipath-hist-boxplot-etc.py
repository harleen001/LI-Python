import matplotlib.pyplot as plt
import pandas as pd


Data={
    "Salary": [25000,30000,70000,45000,32000,61000,29000,38000,31000,45000]
}
df=pd.DataFrame(Data)

#HISTOGRAM
#plt.hist(df['Salary'],bins=5,color='green')  #bins means no of hists
#plt.show()


#BOX PLOT
plt.boxplot(df['Salary'])  #shows min value at one end and max value at other end
plt.show()