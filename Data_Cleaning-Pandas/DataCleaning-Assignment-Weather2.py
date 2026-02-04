import pandas as pd
data = pd.read_csv('weather2.csv')
print(data)

data = data.replace({'TEMPERATURE':'[A-Za-z]','WINDSPEED':'[A-Za-z]'},'',regex=True)
print(data)


d = {'score':['exceptional','average','good','poor','average','exceptional'],
  'student':['Karan','Arpit','Varun','Robin','Akshay','Ankush']}
data = pd.DataFrame(d)
print(data)

data = data.replace(['poor','average','good','exceptional'],[1,2,3,4])
print(data)