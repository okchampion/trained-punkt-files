#This is a little script that trains the punkt tokenizer that comes with NLTK
#To train it, we need a test file that contains one sentence per line. 
#Europarl Corpus is used, hopefully
# import punkt

import nltk
import gc
gc.collect()
# Make a new Tokenizer
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()

# Read in trainings corpus (one example: Slovene)
import codecs
text = codecs.open("TrainingData/europarl-v7.hu-en.hu","Ur","iso-8859-2").read()

# Train tokenizer
tokenizer.train(text)

# Dump pickled tokenizer
import pickle
out = open("hungarian.pickle","wb")
pickle.dump(tokenizer, out)
out.close() 