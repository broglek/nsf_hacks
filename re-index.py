import sys
import glob
import os
import re


amounts = open("ids_and_amounts_sorted")
ids = open("docwords_master_sorted")
output = open("ids_and_amounts_reindex", 'w')
output2 = open("docwords_master_reindex", 'w')

dict_newid = {}
dict_ids = {}
count = 1

for line in amounts:
    x1, x2 = line.strip().split()
    if not(x1 in dict_newid):
        dict_newid[x1] = count
        count += 1
    else:
        dict_newid[x1] = count
    output.write(str(dict_newid[x1]) + " " + str(x2) + '\n')



for line in ids:
    y1, y2, y3 = line.strip().split()
    if y1 in dict_newid:
        output2.write(str(dict_newid[y1]) + " " + y2 + " " + y3 + '\n')
