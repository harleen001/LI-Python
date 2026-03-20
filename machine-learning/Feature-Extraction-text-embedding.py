from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
text_data = ["Machine learning is fun", "Feature extraction is important", "Text data processing"]

        # TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(text_data)
print("TF-IDF matrix shape:", tfidf_matrix.shape)

        # Word Tokenization for Word Embeddings (e.g., using Word2Vec with Gensim)
        # (Requires Gensim library to be installed: pip install gensim)
        # from gensim.models import Word2Vec
        # tokenized_text = [word_tokenize(sentence.lower()) for sentence in text_data]
        # model = Word2Vec(tokenized_text, vector_size=100, window=5, min_count=1, workers=4)
        # word_vector = model.wv['machine']
        # print("Word vector shape:", word_vector.shape)