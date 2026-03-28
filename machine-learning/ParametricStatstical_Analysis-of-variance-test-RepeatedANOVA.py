# Import library
import numpy as np
import pandas as pd
from statsmodels.stats.anova import AnovaRM

# Create the data
dataframe = pd.DataFrame({'Cars': np.repeat([1, 2, 3, 4, 5], 4),
                          'Oil': np.tile([1, 2, 3, 4], 5),
                          'Mileage': [36, 38, 30, 29,
                                      34, 38, 30, 29,
                                      34, 28, 38, 32,
                                      38, 34, 20, 44,
                                      26, 28, 34, 50]})

# Conduct the repeated measures ANOVA
print(AnovaRM(data=dataframe, depvar='Mileage',
              subject='Cars', within=['Oil']).fit())