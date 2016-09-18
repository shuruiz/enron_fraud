#!/usr/bin/python

from sklearn.feature_extraction.text import CountVectorizer

verctorize=CountVectorizer()
string1="hi welcome to the self driving car and this was was was developed by me"
string2="waterloo is some kind of quiet and boring was was"
string3="this is a test from ethan for the self drving car was was was development precesss"

#put strings to a list
string_list=[string1,string2,string3]

bags_of_words=verctorize.fit(string_list)
bags_of_words=verctorize.transform(string_list)#get actual word count

print bags_of_words

#get a tuple  (sting number, word index) + count

print verctorize.vocabulary_.get("was") #return the index of that  word