import pandas as pd
import numpy as np

technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python"],
    'Fee' :[20000,25000,26000,22000],
    'Duration':['30day','40days',np.nan, None],
    'Discount':[1000,2300,1500,1200]
               }

indexes=['r1','r2','r3','r4']
df = pd.DataFrame(technologies,index=indexes)
print(df)


df = pd.DataFrame(technologies,index=indexes)
df1 = df.drop(['r1','r2'])
print("Drop rows from DataFrame:\n", df1)


df = pd.DataFrame(technologies)    #drop by condition check
df1 = df.loc[df["Discount"] >=1500 ]
print(df1)