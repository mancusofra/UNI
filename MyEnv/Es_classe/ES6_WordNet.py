from nltk.corpus import wordnet as wn

'''
#STAMPA DEI sysets
print(wn.synsets('dog'))

print(wn.synsets('dog',wn.VERB))

'''

#STAMAP LA DEFINIZIONE DELLA PAROLA CERCATA
dog = wn.synset('dog.n.01')
print(dog.definition())

#STAMPA DEGLI ESEMPI 
print(dog.examples())

#
print(dog.hypernyms())

#STAMPA LA PAROLA BASE PRESENTE SU WORDNET
print(wn.morphy('abaci'))
