import nltk

nltk.download('punkt_tab')
string = "This is a sentence. Here is another one."
tokens = nltk.word_tokenize(string)
print(tokens)
import nltk

string = "This is a sentence. Here is another one."

# Tokenize into sentences
sents = nltk.sent_tokenize(string)
print(sents)

# Import the spacy module and load the English language model
import spacy
nlp = spacy.load("en_core_web_sm")

# Create a Doc object from the text
text = "This is a sentence. Here is another one."
doc = nlp(text)

# Iterate over the tokens in the Doc and print their text
for token in doc:
    # Each token is an object with various properties and methods
    # The `text` attribute returns the token's text
    print(token.text)

# Iterate over the sentences in the Doc
for sent in doc.sents:
    # Each sentence is a Span object with various properties and methods
    # The `text` attribute returns the sentence's text
    print(sent.text)

# Iterate over the noun chunks in the Doc
for chunk in doc.noun_chunks:
    # Each noun chunk is a Span object with various properties and methods
    # The `text` attribute returns the noun chunk's text
    print(chunk.text)