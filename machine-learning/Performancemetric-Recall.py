import numpy as np

# Example arrays of true and predicted labels
y_true = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1])
y_pred = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0, 0])

# Assume the positive class is labeled as 1 and the negative class is labeled as 0
positive = 1
negative = 0

# Calculate the number of true positives by counting the instances where both the true and predicted labels are positive
tp = np.sum((y_true == positive) & (y_pred == positive))

# Calculate the number of false negatives by counting the instances where the true label is positive but the predicted label is negative
fn = np.sum((y_true == positive) & (y_pred == negative))

# Calculate the recall by dividing the number of true positives by the sum of true positives and false negatives
recall = tp / (tp + fn)

# Print the recall
print(f"Recall: {recall:.4f}")