from sklearn.feature_extraction.text import CountVectorizer

data = ['I love dogs', 'I hate cats', 'Dogs are cute']

 # Create an instance of CountVectorizer
vectorizer = CountVectorizer()

# Apply BoW transformation
bow_features = vectorizer.fit_transform(data)
print(bow_features)