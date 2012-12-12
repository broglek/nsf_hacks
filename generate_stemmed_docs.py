import sys
import glob
import os
import re



input1 = open("words_stemmed.txt")
input2 = open("docwords_master_reindex")
#output1 = open("words_stemmed.txt", 'w')

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
    if(!x2 in stem_dict):
        stem_dict[x2] = index
        index += 1
    
