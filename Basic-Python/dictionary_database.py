import mysql.connector
import pandas as pd
import sqlalchemy as sq
import numpy as np
mycon=sq.create_engine("mysql+pymysql://root:kartik@localhost/uae")


d1={'empid':[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    'Ename':['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
    'Job':['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen'],
    'salary':[55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
    'comm':[100,np.nan,200,np.nan,100,np.nan,500,np.nan,300,500],
    'Deptno':[10,20,10,10,30,10,20,10,30,40]}

df=pd.DataFrame(d1)
print(df)
#print(df.dtypes)
print(df.describe())