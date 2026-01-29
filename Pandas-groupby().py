#groupby can also be used with the help of sum, avg to calculate for specific columns
import pandas as pd
technologies   = ({
    'Courses':["Spark","PySpark","Hadoop","Python","Pandas","Hadoop","Spark","Python","NA"],
    'Fee' :[22000,25000,23000,24000,26000,25000,25000,22000,1500],
    'Duration':['30days','50days','55days','40days','60days','35days','30days','50days','40days'],
    'Discount':[1000,2300,1000,1200,2500,None,1400,1600,0]
          })
df = pd.DataFrame(technologies)
print("Create DataFrame:\n", df)


df2 =df.groupby(['Courses']).sum()
print("Get sum of grouped data:\n", df2)   #data of specific courses got combined


df2 = df.groupby(['Courses', 'Duration']).sum()
print("Get sum of groupby multiple columns:\n", df2)