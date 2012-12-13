import sys
import glob
import os
import re

input1 = open("ids_and_amounts_buckets")
input2 = open("docwords_master_stemmed")

#output1 = open("ids_and_amounts_1000", 'w')
output2 = open("docwords_master_stemmed_1000", 'w')


#for line in input1:
#    x1, x2 = line.strip().split()
#    if(float(x1) <= 1000):
#        output1.write(line)

for line in input2:
    y1, y2, y3 = line.strip().split()
    if(float(y1) <= 1000):
        output2.write(line)
