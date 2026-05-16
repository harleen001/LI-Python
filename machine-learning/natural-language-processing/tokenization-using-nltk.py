import nltk
import spacy

# 1. FIX: NLTK requires 'punkt' (or 'punkt_tab') for tokenization
nltk.download('punkt')
nltk.download('punkt_tab')

string = "This is a sentence. Here is another one."

# NLTK Word Tokenization
tokens = nltk.word_tokenize(string)
print(f"NLTK Tokens: {tokens}")

# NLTK Sentence Tokenization
sents = nltk.sent_tokenize(string)
print(f"NLTK Sentences: {sents}")


# 2. FIX: Ensure the model is loaded. 
# Note: You must run 'python -m spacy download en_core_web_sm' in your terminal first.
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback if model isn't installed
    print("Downloading spaCy model...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

doc = nlp(string)

print("\n--- spaCy Analysis ---")
# Token Text
print("Tokens:", [token.text for token in doc])

# Sentence Text
print("Sentences:", [sent.text for sent in doc.sents])

# Noun Chunks
print("Noun Chunks:", [chunk.text for chunk in doc.noun_chunks])