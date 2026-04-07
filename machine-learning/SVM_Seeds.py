import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 1. Load the Seeds Dataset (hosted on UCI)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00236/seeds_dataset.txt"
# Data is tab-separated with multiple spaces
df = pd.read_csv(url, sep='\s+', header=None)

# 2. Name the columns
df.columns = ['Area', 'Perimeter', 'Compactness', 'Kernel_Length', 
              'Kernel_Width', 'Asymmetry_Coeff', 'Groove_Length', 'Species']

# 3. Simplify for Visualization
# We'll pick 2 features so we can draw the best-fit lines in 2D
X = df[['Area', 'Asymmetry_Coeff']].values 
y = df['Species'].values

# 4. Split and Scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. Train Linear SVM
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# 6. Create the Best-Fit Decision Boundary Plot
# Create a grid to plot in
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                     np.arange(y_min, y_max, 0.02))

# Predict across the grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 7. Final Plot
plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.3, cmap='viridis') # The decision regions
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', cmap='viridis')

plt.title('SVM Best-Fit Boundaries: Wheat Seeds Classification')
plt.xlabel('Area (Scaled)')
plt.ylabel('Asymmetry Coefficient (Scaled)')
plt.show()

print(f"Model Accuracy: {accuracy_score(y_test, model.predict(X_test))*100:.2f}%")