import nltk
#import e inizializzazione di porter
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
#import e inizializzazione di lancester
from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()


text = "This is a test"
tokens = nltk.word_tokenize(text)

#stampa dei due stamming diversi (output uguale)
print([porter.stem(t) for t in tokens])
print([lancaster.stem(t) for t in tokens])
