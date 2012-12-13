import sys
import glob
import os
import re
from stemming.porter2 import stem


input1 = open("words_stemmed.txt")

count_dict = {}

for line in input1:
    x1, x2 = line.strip().split()
    count_dict[x2] = 1


print str(len(count_dict.keys()))
