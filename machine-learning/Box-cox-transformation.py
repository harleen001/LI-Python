from scipy.stats import boxcox
import numpy as np
data = np.array([1, 2, 3, 10, 100])
data_transformed, _ = boxcox(data)
print(data_transformed)