import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')
data = 'pulsar_stars.csv'
df = pd.read_csv(data)

df.shape # view dimensions of dataset
df.head() #lets preview a dataset