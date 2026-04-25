# Sample dataset about Japanese tea ceremony
import evaluate
references = [
    "The Japanese tea ceremony is a profound cultural practice emphasizing harmony and respect.",
    "Matcha is carefully prepared using traditional methods in a tea ceremony.",
    "The tea master meticulously follows precise steps during the ritual."
]

predictions = [
    "Japanese tea ceremony is a cultural practice of harmony and respect.",
    "Matcha is prepared using traditional methods in tea ceremonies.",
    "The tea master follows precise steps during the ritual."
]

# Accuracy and F1 Score
accuracy_metric = evaluate.load("accuracy")
f1_metric = evaluate.load("f1")

# Simulate binary classification (e.g., ceremony vs. non-ceremony)
labels = [1, 1, 1]  # All are about tea ceremony
pred_labels = [1, 1, 1]  # Model predicts all correctly

accuracy = accuracy_metric.compute(predictions=pred_labels, references=labels)
f1 = f1_metric.compute(predictions=pred_labels, references=labels, average='weighted')

print("Accuracy:", accuracy)
print("F1 Score:", f1)

# Perplexity (using a small GPT2 language model)
perplexity_metric = evaluate.load("perplexity", module_type="metric")
perplexity = perplexity_metric.compute(
    predictions=predictions,
    model_id='gpt2'  # Using a small pre-trained model
)
print("Perplexity:", perplexity)