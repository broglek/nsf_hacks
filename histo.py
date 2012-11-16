import sys
import glob
import os
import re
import numpy
import matplotlib.pyplot as plt


def save(path):
    fig = plt.gcf()
    fig.set_figwidth(16.5)
    fig.set_figheight(12.75)
    plt.savefig(path)
    plt.clf()
    plt.cla()
    plt.close()

dollaz = open("ids_and_amounts_reindex").readlines()
f = []

for line in dollaz:
    x1, x2 = line.strip().split()
    f.append(x2)

f = numpy.array(f, numpy.int)
n, bins, patches = plt.hist(f, bins=100, facecolor='green', alpha=0.75, range=(0,1000000))
save("histo")
