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

id1 = open("ids_and_amounts_random_1000", 'w')
doc1 = open("docwords_master_random_1000", 'w')

id2 = open("ids_and_amounts_random_2000", 'w')
doc2 = open("docwords_master_random_2000", 'w')

id5 = open("ids_and_amounts_random_5000", 'w')
doc5 = open("docwords_master_random_5000", 'w')

id10 = open("ids_and_amounts_random_10000", 'w')
doc10 = open("docwords_master_random_10000", 'w')


docs_wanted = random.sample(docs, 10000)
#docs_wanted_10 = random.sample(docs, 10000)
#docs_wanted_1 = docs_wanted_10[:1000]
#docs_wanted_2 = docs_wanted_10[:2000]
#docs_wanted_5 = docs_wanted_10[:5000]

docs_wanted_10 = {}
docs_wanted_1 = {}
docs_wanted_2 = {}
docs_wanted_5 = {}

for i in docs_wanted[:1000]:
    docs_wanted_1[i] = 1

for i in docs_wanted[:2000]:
    docs_wanted_2[i] = 1

for i in docs_wanted[:5000]:
    docs_wanted_5[i] = 1

for i in docs_wanted[:10000]:
    docs_wanted_10[i] = 1

print "finished randoming\n"
print str(len(docs_wanted_10.keys()))

for line in input1:
    x1, x2 = line.strip().split()
    if(float(x1) in docs_wanted_10):
        id10.write(line)
    if(float(x1) in docs_wanted_5):
        id5.write(line)
    if(float(x1) in docs_wanted_2):
        id2.write(line)
    if(float(x1) in docs_wanted_1):
        id1.write(line)

print "finished id files\n"

for line in input2:
    y1, y2, y3 = line.strip().split()
    if(float(y1) in docs_wanted_10):
        doc10.write(line)
    if(float(y1) in docs_wanted_5):
        doc5.write(line)
    if(float(y1) in docs_wanted_2):
        doc2.write(line)
    if(float(y1) in docs_wanted_1):
        doc1.write(line)
