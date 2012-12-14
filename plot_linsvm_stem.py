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


#1000,2000,5000
test = [1.0 - 0.2100, 1.0 - 0.2116, 1.0 - 0.2308, 1.0 - 0.3015]
train = [1.0 - 0.9810, 1.0 - 0.9685, 1.0 - 0.9502, 1.0 - 0.8886]

x = [1000, 2000, 5000, 10000]

l1, l2 = plt.plot(x, train, x, test)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))

ftsz = "xx-large"

plt.title("Linear SVM Training vs. Test Set Error (Stemmed words)", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Error", fontsize = ftsz)

save("linsvm_stem_train_vs_test")
