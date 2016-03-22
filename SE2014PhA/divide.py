import nltk
from nltk import *
from nltk.corpus import stopwords
import re
import string

f = open('sentences.txt');
vocabulary = []
for line in f:
    line = line.strip()
    pattern = r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
    divided = re.findall(pattern, line)
    for word in divided:
        word = word.strip()
        if word in list(string.punctuation):
            divided.remove(word)
    #print(divided)
    vocabulary = vocabulary + divided
f.close()
length = vocabulary.__len__()
#freq = FreqDist(vocabulary)
print("divided length")
print(len(vocabulary))

filter_vo = vocabulary[:]
for word in filter_vo:
    if word in stopwords.words('english'):
        filter_vo.remove(word)
print("filtered length")
print(len(filter_vo))


porter = nltk.PorterStemmer()
stemmed_vo = [porter.stem(w.lower()) for w in filter_vo]
print("stemmed length")
print(len(stemmed_vo))

#wnl = nltk.WordNetLemmatizer()
#lemmatized_vo = [wnl.lemmatize(t) for t in stemmed_vo]
#print("lemmatized length")
#print(len(lemmatized_vo))

rm_dup_vo = {}.fromkeys(stemmed_vo).keys()
print("remove duplicate length")
print(len(rm_dup_vo))
#print(rm_dup_vo)

output_file = open('pre_words.txt', 'w')
for word in rm_dup_vo:
    output_file.write(word + '\n')
output_file.close()





    

