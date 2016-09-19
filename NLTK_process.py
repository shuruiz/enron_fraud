#!/usr/bin/python

import nltk
from nltk.corpus import stopwords


sw=stopwords.words("english")
#print sw

#use stemmer in nltk
from nltk.stem.snowball import SnowballStemmer
stemmer=SnowballStemmer("english")
print stemmer.stem("responsiveness")