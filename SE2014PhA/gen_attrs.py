import nltk
from nltk import *
from nltk.corpus import stopwords
import re
import string

pre = open('pre_words.txt', 'r')
sentences = open('sentences.txt', 'r')
out = open('attrs.txt', 'w')

vocabulary = []
for line in pre:
    vocabulary.append(line.strip())

print(vocabulary)
porter = nltk.PorterStemmer()
for line in sentences:
    pattern = r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"
    divided = re.findall(pattern, line)
    stemmed = [porter.stem(w.lower()) for w in divided]
    i = 1
    for vo in vocabulary:
        if vo in stemmed:
            out.write(str(i))
            out.write(':')
            out.write(str(1))
            out.write(' ')
        else:
            out.write(str(i))
            out.write(':')
            out.write(str(0))
            out.write(' ')
        i = i + 1
    out.write('\n')
out.close()
pre.close()
sentences.close()
        
