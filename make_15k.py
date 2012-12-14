import sys
import glob
import os
import re
import random

input1 = open("ids_and_amounts_buckets")
docs = []    
input2 = open("docwords_master_reindex")
for line in input1:
    y1, y2 = line.strip().split()
    docs.append(float(y1))

input1 = open("ids_and_amounts_buckets")

id10 = open("ids_and_amounts_random_10000")
doc10 = open("docwords_master_random_10000")

id15 = open("ids_and_amounts_random_15000", 'w')
doc15 = open("docwords_master_random_15000", 'w')


#docs_wanted = random.sample(docs, 10000)
#docs_wanted_10 = random.sample(docs, 10000)
#docs_wanted_1 = docs_wanted_10[:1000]
#docs_wanted_2 = docs_wanted_10[:2000]
#docs_wanted_5 = docs_wanted_10[:5000]

docs_wanted_15 = {}


for line in id10:
    x1, x2 = line.strip().split()
    docs_wanted_15[float(x1)] = 1

count = 0
while count < 5000:
    newdoc = (random.sample(docs, 1))
    docnum = newdoc[0]
    if not (float(docnum)) in docs_wanted_15:
        docs_wanted_15[float(newdoc[0])] = 1
        count += 1

print "finished randoming\n"
print str(len(docs_wanted_15.keys()))

for line in input1:
    x1, x2 = line.strip().split()
    if(float(x1) in docs_wanted_15):
        id15.write(line)

print "finished id files\n"

for line in input2:
    y1, y2, y3 = line.strip().split()
    if(float(y1) in docs_wanted_15):
        doc15.write(line)
