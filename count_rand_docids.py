import sys
import glob
import os
import re
from stemming.porter2 import stem


input1 = open("docwords_master_random_1000")

count_dict = {}

for line in input1:
    x1, x2, x3 = line.strip().split()
    count_dict[x1] = 1


print str(len(count_dict.keys()))
