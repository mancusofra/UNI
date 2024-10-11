
import nltk
#nltk.download('punkt_tab')
import yake

#lettura del testo dal sito
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')
#print(f'1- Parole estratte: {len(raw)}')


#ELIMINAZIONE STOPWORDS
tokens = nltk.word_tokenize(raw)
from nltk.corpus import stopwords
no_stop = [t for t in tokens if not t in stopwords.words('english')]
#print(f'2- Parole stopwords: {len(no_stop)}')

'''
#STEMMING
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(t) for t in no_stop]
print(f'3- Stemming: {len(stemmed)}') '''

kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(tokens)
#print(keywords)