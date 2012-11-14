import sys
import glob
import os
import re


amounts = open("amount_list")
ids = open("idnsfid_master.txt")

dic = {}

for line in amounts:
    x1, x2 = line.strip().split()
    dic[x1] = ("BAD", x2)

for line in ids:
    print line
    y1, y2 = line.strip().split()
    dic[y2] = (y1, dic[y2][1])

output = open("ids_and_amounts", 'w')

for key in dic.keys():
    if(dic[key][0] != "BAD"):
        output.write(str(dic[key][0]) + " " + str(dic[key][1]) + '\n')


