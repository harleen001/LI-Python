import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
from io import StringIO
import matplotlib.pyplot as plt
from sklearn import tree
from IPython.display import Image
import pydotplus

# 1. FIXED DATA LOADING:
# Use header=0 to tell pandas the first row contains names, then names= to OVERWRITE them.
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv("diabetes.csv", header=0, names=col_names) 

# 2. FEATURE SELECTION
feature_cols = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X = pima[feature_cols] 
y = pima.label 

# 3. SPLIT & TRAIN
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# 4. PREDICT & ACCURACY
y_pred = clf.predict(X_test)    
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# 5. VISUALIZATION
plt.figure(figsize=(15,10))

# Plot the tree
tree.plot_tree(clf, 
               feature_names=feature_cols,  
               class_names=['0','1'],
               filled=True, 
               rounded=True, 
               fontsize=10)

# Save and Show
plt.savefig('diabetes_plot.png')
plt.show()