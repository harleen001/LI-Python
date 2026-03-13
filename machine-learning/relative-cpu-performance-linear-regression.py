import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
filename = "machine-test.csv"

df = pd.read_csv(filename, header = None)

print("Shape of dataframe df: {}".format(df.shape))
col_names = ['Vendor Name','Model Name', 'MYCT', 'MMIN', 'MMAX', 'CACH','CHMIN', 'CHMAX', 'PRP', 'ERP' ]
df.columns = col_names

#finding categorical variables and searching them
categorical = [col for col in df.columns if df[col].dtype=='O']
print('There are {} categorical variables'.format(len(categorical)))

print(categorical)


df['Vendor Name'].value_counts()
print('Number of unique Model Names: ', len(df['Model Name'].unique()))
print('Number  of instances of models: ', len(df))


#finding numerical variables and searching them
numerical = [col for col in df.columns if df[col].dtype!='O']
print('There are {} numerical variables'.format(len(numerical)))
print(numerical)

# divinding the data now for linear regression
df_cat = df.iloc[:,:2]
df_num = df.iloc[:, 2:]
X = df_num.iloc[:,0:6]
y = df_num.iloc[:,-1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.3,random_state = 0)
X_train.shape, y_train.shape
X_test.shape, y_test.shape
# let's inspect the training dataframe

print(X_train.head())
X_train.describe()


# Feature Scaling - I use the StandardScaler from sklearn

# import the StandardScaler class from preprocessing library
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()# instantiate an object scaler

X_train = scaler.fit_transform(X_train) # fit the scaler to the training set and then transform it
X_test = scaler.transform(X_test) # transform the test set

# fit the linear regression model
# import the LinearRegression class from linear_model library
from sklearn.linear_model import LinearRegression


lr = LinearRegression() # instantiate an object lr
lr.fit(X_train, y_train)  # Train the model using the training sets
y_pred = lr.predict(X_test)
lr.predict(X_test)[0:5]

print("Number of coefficients:", len(lr.coef_))

print("Estimated coefficients: {}".format(lr.coef_))

print("Estimated intercept: {}".format(lr.intercept_))



