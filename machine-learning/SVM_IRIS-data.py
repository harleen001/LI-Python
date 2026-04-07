import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# 1. Load data (Using only 2 features for 2D plotting)
iris = datasets.load_iris()
X = iris.data[:, :2] # We only take Sepal Length and Sepal Width
y = iris.target

# To make it "simple," we only look at two classes (Binary Classification)
X = X[y != 2]
y = y[y != 2]

# 2. Build and Fit the SVM Model
# 'C' is the penalty for misclassification (like your Ridge/Lasso alpha)
model = SVC(kernel='linear', C=1.0)
model.fit(X, y)

# 3. Create a Mesh Grid to draw the "Best Fit" Decision Boundary
h = .02  # step size in the mesh
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

# 4. Predict across the entire grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 5. Plotting
plt.figure(figsize=(10, 6))

# Plot the decision boundary (the colored regions)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.3)

# Plot the best-fit line (the hyperplane)
# This is the "Street" SVM creates
plt.contour(xx, yy, Z, colors='k', levels=[0], linestyles=['-'])

# Plot the actual data points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, edgecolors='k')

plt.title('SVM Best-Fit Line (Linear Decision Boundary)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()