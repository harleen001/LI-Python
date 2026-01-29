
import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Python","pandas"],
    'Fee' :[20000,25000,22000,30000],
    'Duration':['30days','40days','35days','50days'],
              }
index_labels=['r1','r2','r3','r4']
df1 = pd.DataFrame(technologies,index=index_labels)
print("First DataFrame:\n", df1)
technologies2 = {
    'Courses':["Spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
              }
index_labels2=['r1','r6','r3','r5']
df2 = pd.DataFrame(technologies2,index=index_labels2)
print("Second DataFRame:\n", df2)

df3=df1.join(df2, lsuffix="_left", rsuffix="_right")

# Pandas Inner join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='inner')

# Pandas Right join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='right')

# Pandas outer join DataFrames
df3=df1.join(df2, lsuffix="_left", rsuffix="_right", how='outer')

# Pandas join on columns
df3=df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')