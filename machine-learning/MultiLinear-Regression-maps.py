import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    'Price': [200, 300, 400, 500, 600],
    'Size': [1000, 1500, 2000, 2500, 3000],
    'Bedrooms': [2, 3, 3, 4, 5],
    'Age': [10, 5, 8, 2, 1]
}
df = pd.DataFrame(data)

# Create Correlation Matrix
corr_matrix = df.corr()

# Plot Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()






