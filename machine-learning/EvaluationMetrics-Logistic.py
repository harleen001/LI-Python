from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
# Generate some dummy data
X = np.random.rand(100, 5)  # 100 samples, 5 features
y = np.random.randint(0, 2, 100) # 100 labels (binary classification)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a simple model (e.g., Logistic Regression)
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1] # Probabilities for ROC curve

# Accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Precision
precision = metrics.precision_score(y_test, y_pred)
print(f"Precision: {precision:.4f}")

# Recall (Sensitivity)
recall = metrics.recall_score(y_test, y_pred)
print(f"Recall (Sensitivity): {recall:.4f}")

# F1-score
f1 = metrics.f1_score(y_test, y_pred)
print(f"F1-score: {f1:.4f}")

# Confusion Matrix
conf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", conf_matrix)

# Classification Report (combines precision, recall, f1-score, and support for each class)
class_report = metrics.classification_report(y_test, y_pred)
print("\nClassification Report:\n", class_report)

# ROC AUC Score
roc_auc = metrics.roc_auc_score(y_test, y_pred_proba)
print(f"\nROC AUC Score: {roc_auc:.4f}")