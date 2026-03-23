from sklearn.preprocessing import PowerTransformer
import numpy as np
data = np.array([-1, 0, 1, 10, 100]).reshape(-1, 1)
transformer = PowerTransformer(method='yeo-johnson')
data_transformed = transformer.fit_transform(data)
print(data_transformed)