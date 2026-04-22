import numpy as np
from sklearn import preprocessing
from sklearn.datasets import fetch_california_housing

# create the DataFrame
california_housing = fetch_california_housing(as_frame=True)

# print the dataset description
print(california_housing.DESCR)