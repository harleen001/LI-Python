import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")
from sklearn.preprocessing import QuantileTransformer
import pandas as pd
data = pd.DataFrame({'Feature': [1, 2, 3, 10, 100]})
transformer = QuantileTransformer(output_distribution='normal')
data['Transformed_Feature'] = transformer.fit_transform(data[['Feature']])
print(data)