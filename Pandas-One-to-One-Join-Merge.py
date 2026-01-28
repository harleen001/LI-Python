#merge one to one
import pandas as pd
d={'empid':pd.Series([1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'Ename':pd.Series(['Smith','Blake','King','Harry','Mohit','Harry','Pawan','perry','jerry','gagan'],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'Job':pd.Series(['manager','salesmen','president','clerk','programmer','clerk','programmer','clerk','manager','salesmen',],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'salary':pd.Series([55000,65000,85000,25000,55000,25000,65000,25000,35000,45000],
                     index=[1,2,3,4,5,6,7,8,9,10]),
                     'comm':pd.Series([100,200,100,500,300,500],
                     index=[1,3,5,7,9,10]),
                     'Deptno':pd.Series([10,20,10,10,30,10,20,10,30,40],
                     index=[1,2,3,4,5,6,7,8,9,10])
                     }
df=pd.DataFrame(d)
print(df)

df1=pd.DataFrame(
    {
        "Name":["Sharan","Jasleen","Jagroop","Seema","Meena","Teena","Deena","Taj","Raj","Pawan"],
        "Rollno":[1,2,3,4,5,6,7,8,9,10],
        "Gender":["Female","Female","Male","Female","Female","Female","Female","Female","Male","Male"],
        "English":[90,56,67,87,67,89,89,89,78,90],
     "Maths":[45,56,67,87,67,89,89,89,78,90],
     "Science":[45,53,67,86,67,84,89,89,73,90],
     "Hindi":[56,56,65,87,68,89,86,89,73,95],
     "Punjabi":[66,56,64,87,69,89,87,89,78,93]


    }

)
print(df1)
print()
print(df.merge(df1, left_on='Ename', right_on='Name'))