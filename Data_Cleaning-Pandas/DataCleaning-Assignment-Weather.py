import numpy as np
import pandas as pd
data = pd.read_csv('weather_data.csv')
print(data)

data.shape
data.info()


data.replace(-1, np.nan, inplace=True)    #Replaces all instances of -1 with NaN
print(data)

data = data.replace(-99999,value=np.nan)
print(data)


print(data.info())

data=data.replace([32.0,7.0],value=99)
print(data)

data.replace({'temperature':99.0,'windspeed':np.nan,'event':'0'},100,inplace=True)
print(data)

print("-----------replacing with dictionary-------------------")
data = data.replace({np.nan:69,'0':'Sunny'})
print(data)