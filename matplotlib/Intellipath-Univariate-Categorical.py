import matplotlib.pyplot as plt
import pandas as pd

#Univariate (Categorical data)
Data={
    "Salary": [25000,30000,70000,45000,32000,61000,29000,38000,31000,45000,15000,23000]
}
df=pd.DataFrame(Data)
df['Dept']=['HR','It','Marketing','HR','UI','It']*2

print(df.head())   #categorically presented data

#to visualize a categorical column we can use PIE CHART
#FIRST COUNT NUMBER OF UNIQUE VALUES

count=df["Dept"].value_counts()
print(count)

plt.pie(count,labels=count.index,autopct="%1.0f",explode=[0,0.1,0,0.2])    #EXPLODES OUT BY SPECIFIC DISTANCE FROM OTHERS

#creates a pie chart, %1.1f is used for percentage multiplication upto 1 decimal

#COUNT PLOT
#plt.bar(count.index,count, color=['green','black','red'])   #simple bars printed
#plt.axis("equal") #puts pie chart in complete circle
plt.show()