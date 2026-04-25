from sklearn.metrics import accuracy_score

# Example arrays of true and predicted labels
y_true = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1])
y_pred = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0, 0])

# Calculate accuracy using Scikit-learn
accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy:.2f}")