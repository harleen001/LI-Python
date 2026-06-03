from rake_nltk import Rake
import nltk

# This line only needs to run successfully once on your machine
nltk.download('stopwords')

rake = Rake()
rake.extract_keywords_from_text("RAKE is used for extracting the keywords from the text, It works irrespective of the text’s Domain")
print(rake.get_ranked_phrases())  