import nltk

text = "This is a test"
tokens = nltk.word_tokenize(text)

print(nltk.pos_tag(tokens))

#nltk.help.upenn_tagset() #stampa la legenda dei significati delle sigle