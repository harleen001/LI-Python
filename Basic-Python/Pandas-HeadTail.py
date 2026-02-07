import pandas as pd

d1={'empid':[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
    'Ename':['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
    'Job':['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen'],
    'salary':[55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
    'comm':[100,'Nan',200,'Nan',100,'Nan',500,'Nan',300,500],
    'Deptno':[10,20,10,10,30,10,20,10,30,40]}

df=pd.DataFrame(d1)

#print(df.head())
print("----------------------------------------------------------")
#print(df.tail())
print("----------------------------------------------------------")
#print(df.head(7))


df.info()  #Gives information about the table contents
df.dtypes  #tells datatype of each named object


pd.set_option('display.max_columns',4)    #displays only maximum 4 columns
print(df.head())