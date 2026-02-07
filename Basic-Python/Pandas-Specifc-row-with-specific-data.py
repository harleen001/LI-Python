import pandas as pd
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
d={'empid':pd.Series([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],index=[1,2,3,4,5,6,7,8,9,10]),
   'Ename':pd.Series(['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],index=[1,2,3,4,5,6,7,8,9,10]),
   'Job':pd.Series(['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen',],index=[1,2,3,4,5,6,7,8,9,10]),
   'salary':pd.Series([55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],index=[1,2,3,4,5,6,7,8,9,10]),
   'comm':pd.Series([100,200,100,500,300,500],index=[1,3,5,7,9,10]),
   'Deptno':pd.Series([10,20,10,10,30,10,20,10,30,40],index=[1,2,3,4,5,6,7,8,9,10])}
df=pd.DataFrame(d)

ser_result=df[df["Deptno"]==10]
print(ser_result)
print("------------------------------------------------------")
ser_result1=df[df["Job"]=='manager']
print(ser_result1)
print("--------------------------------------------------------")
ser_result2=df[(df["Deptno"]==10) | (df["Deptno"]==20)]
print(ser_result2)
print("----------------------------------------------------------")
ser_result3=df[(df["salary"]>=45000) & (df["salary"]<=65000)]
print(ser_result3)
#df.to_excel('SatyamEmployee.xlsx', sheet_name='Employee')
df.to_json('SatyamEmployee.json')