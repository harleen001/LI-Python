from sklearn.preprocessing import StandardScaler
import numpy as np
X=np.array([[1.0],[200.0],[2.0],[300.0],[3.0]])
scalar=StandardScaler()
#fit the scalar data
X_scalad=scalar.fit_transform(X)
print(X_scalad)
from sklearn.preprocessing import MinMaxScaler
scalar=MinMaxScaler()

X_normalized=scalar.fit_transform(X)
print(X_normalized)