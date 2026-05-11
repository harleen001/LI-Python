import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
from warnings import filterwarnings
filterwarnings('ignore')
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

#creating strings
text = "language"
print(text)
print(3*text)

"language" + "processing"  #concatenation

"L" + text[1:]  #slicing


#loop
texts =  ["natural","language","processing"]
for text in texts:
    print("text:",text)


for text in texts:
    print("-", text[0:], sep = "")


print(*enumerate(texts))
for text in enumerate(texts):
    print(text)

for text in enumerate("texts"):
    print(text)

text="Natural Language"
print(text.upper().lower())
print(text.lower().upper())
print(text.swapcase())