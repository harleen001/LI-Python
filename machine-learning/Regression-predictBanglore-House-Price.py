import pandas as pd
path = r"https://drive.google.com/uc?export=download&id=1xxDtrZKfuWQfl-6KA9XEd_eatitNPnkB"
df = pd.read_csv(path)
df.head()

#split data
X = df.drop('price', axis=1)
y = df['price']

print('Shape of X = ', X.shape)
print('Shape of y = ', y.shape)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=51)

print('Shape of X_train = ', X_train.shape)
print('Shape of y_train = ', y_train.shape)
print('Shape of X_test = ', X_test.shape)
print('Shape of y_test = ', y_test.shape)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train = sc.transform(X_train)
X_test = sc.transform(X_test)


#model training
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train, y_train)

print(lr.coef_)
print(lr.intercept_)

#predicting value of home and test
X_test[0, :]

lr.predict([X_test[0, :]])
lr.predict(X_test)
y_test

lr.score(X_test, y_test)

from sklearn.linear_model import Ridge, Lasso

rd = Ridge()
rd.fit(X_train,y_train)
rd.score(X_test, y_test)

ls = Lasso()

ls.fit(X_train,y_train)

ls.score(X_test, y_test)
rd2 = Ridge(alpha = 2)

rd2.fit(X_train,y_train)

rd2.score(X_test, y_test)
ls2 = Lasso(alpha=2)

ls2.fit(X_train,y_train)

ls2.score(X_test, y_test)
ls3 = Lasso(alpha=3)

ls3.fit(X_train,y_train)

ls3.score(X_test, y_test)