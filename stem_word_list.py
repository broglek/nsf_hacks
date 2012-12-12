import sys
import glob
import os
import re
from stemming.porter2 import stem


input1 = open("words.txt")
output1 = open("words_stemmed.txt", 'w')



for line in input1:
    x1, x2 = line.strip().split()
    new_word = stem(x2)
    output1.write(x1 + " " + new_word + '\n')
