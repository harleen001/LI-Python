import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Load the Dataset
iris = datasets.load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])

# 2. Standardize the features
# It is best practice to keep the column names for clarity
scaler = StandardScaler()
scaled_values = scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled_values, columns=df.columns)

# 3. Check Correlation BEFORE PCA
plt.figure(figsize=(8, 4))
plt.title("Correlation Before PCA (High Collinearity)")
sns.heatmap(df_scaled.corr(), annot=True, cmap='coolwarm')
plt.show()

# 4. Applying PCA
# We use 3 components as requested
pca = PCA(n_components=3)
pca_data = pca.fit_transform(df_scaled)

# Create a DataFrame for the Principal Components
df_pca = pd.DataFrame(pca_data, columns=['PC1', 'PC2', 'PC3'])

# 5. Check Correlation AFTER PCA
# Note: Correlations will be ~0 because PCs are orthogonal
plt.figure(figsize=(8, 4))
plt.title("Correlation After PCA (Orthogonal Components)")
sns.heatmap(df_pca.corr(), annot=True, cmap='coolwarm')
plt.show()

# Display results
print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print(df_pca.head())