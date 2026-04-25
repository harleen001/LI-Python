import numpy as np

# Example arrays of true and predicted labels
y_true = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1])
y_pred = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0, 0])

# Calculate the number of correct predictions by comparing the two columns element-wise
correct = np.sum(y_true == y_pred)

# Calculate the total number of predictions by taking the length of either column
total = len(y_true)

# Calculate the accuracy by dividing the number of correct predictions by the total number of predictions
accuracy = correct / total

# Print the accuracy
print(f"Accuracy: {accuracy:.4f}")