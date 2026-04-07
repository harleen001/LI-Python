import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# 1. Load dataset (Handling potential path issues)
try:
    data = 'machine-learning/pulsar_stars.csv'
    df = pd.read_csv(data)
except FileNotFoundError:
    data = 'pulsar_stars.csv'
    df = pd.read_csv(data)

# 2. Data Cleaning: Strip spaces and rename columns
df.columns = df.columns.str.strip()
df.columns = ['IP Mean', 'IP Sd', 'IP Kurtosis', 'IP Skewness', 
              'DM-SNR Mean', 'DM-SNR Sd', 'DM-SNR Kurtosis', 'DM-SNR Skewness', 'target_class']

# 3. Data Inspection & Stats
print(f"Dataset Shape: {df.shape}\n")
print("--- Target Class Distribution ---")
# Fix: Using standard len() instead of np.float to avoid AttributeError
print(df['target_class'].value_counts() / len(df), "\n")

print("--- Summary Statistics ---")
print(round(df.describe(), 2))


# 5. Visualization Section B: Histograms (Distribution Check)
plt.figure(figsize=(24, 20))

# Loop through features to create histograms
for i, col in enumerate(df.columns[:-1], 1):
    plt.subplot(4, 2, i)
    fig = df[col].hist(bins=20, color='skyblue', edgecolor='black')
    fig.set_title(f'Distribution of {col}')
    fig.set_xlabel(col)
    fig.set_ylabel('Number of pulsar stars')

plt.tight_layout()
plt.show()