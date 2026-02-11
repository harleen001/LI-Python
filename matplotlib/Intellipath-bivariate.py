#Bivariate is relationship between two features or two columns
import matplotlib.pyplot as plt
import pandas as pd

Data={
    "Salary": [25000,30000,70000,45000,32000,61000,29000,38000,31000,45000,15000,23000]
}
df=pd.DataFrame(Data)
df['Dept']=['HR','It','Marketing','HR','UI','It']*2


df["Age"]=[20,12,32,43,24,32,52,33,25,34,25,23]

#Scatter plot to see if salary increases with age or not
plt.scatter(df['Age'],df['Dept'],color='orange')
plt.show()
