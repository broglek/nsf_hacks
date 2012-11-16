import sys
import glob
import os
import re
import math


amounts = open("ids_and_amounts_reindex")
output = open("ids_and_amounts_buckets", 'w')

dict_newid = {}
dict_ids = {}
count = 1

for line in amounts:
    x1, x2 = line.strip().split()
    if math.ceil(float(x2) / 50000) <= 20:
        output.write(x1 + " " + str(math.ceil(float(x2) / 50000)) + '\n')
    else:
        output.write(x1 + " " + "21" + '\n')

