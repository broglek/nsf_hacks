import sys
import glob
import os
import re



input1 = open("words_stemmed.txt")
input2 = open("docwords_master_random_15000")
output1 = open("docwords_master_random_stem_15000", 'w')

#numbering dict is lookup old number, get stemmed word.
#stem_dict is lookup word, get new number.
#docs_dict is lookup (docid, wordid), get count.
numbering_dict = {}
stem_dict = {}
docs_dict = {}
index = 1

for line in input1:
    x1, x2 = line.strip().split()
    numbering_dict[x1] = x2
    if(not x2 in stem_dict):
        stem_dict[x2] = index
        index += 1
    
for line in input2:
    x1, x2, x3 = line.strip().split()
    stemmed_word = numbering_dict[x2]
    new_index = stem_dict[stemmed_word]
    if (x1,new_index) in docs_dict:
        docs_dict[(x1,new_index)] += x3
    else:
        docs_dict[(x1,new_index)] = x3


for key in sorted(docs_dict.keys(), key=lambda x: float(x[0])):
    output1.write(str(key[0]) + " " + str(key[1]) + " " + str(docs_dict[key]) + '\n')
