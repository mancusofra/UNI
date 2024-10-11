import nltk
from nltk.corpus import stopwords

wnl = nltk.WordNetLemmatizer()

text = "This is a test"
tokens = nltk.word_tokenize(text)

for t in tokens:
    if not t in stopwords.words('english'):
        print(wnl.lemmatize(t))    