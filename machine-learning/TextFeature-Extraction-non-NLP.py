from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Assuming 'data' DataFrame is available from previous cells,
# add a sample 'text_column' for demonstration
if 'text_column' not in data.columns:
    data['text_column'] = [
        'This is a sample text for the first row.',
        'Another example text for the second row.',
        'Third text data for TF-IDF embedding.'
    ]

vectorizer = TfidfVectorizer()
tfidf_features = vectorizer.fit_transform(data['text_column'])

print("TF-IDF Features shape:", tfidf_features.shape)
print("TF-IDF Features (sparse matrix):")
print(tfidf_features)
