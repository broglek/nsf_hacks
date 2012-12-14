import sys
import glob
import os
import re
import numpy
import matplotlib
matplotlib.use('PDF')
import matplotlib.pyplot as plt


def save(path):
    fig = plt.gcf()
    fig.set_figwidth(16.5)
    fig.set_figheight(12.75)
    plt.savefig(path)
    plt.clf()
    plt.cla()
    plt.close()

ftsz = "xx-large"
#1000,2000,5000
test = [1.0 - 0.2746, 1.0 - 0.2735, 1.0 - 0.2796, 1.0 - 0.2807]
train = [1.0 - 1.000, 1.0 - 0.9995, 1.0 - 0.9984, 1.0 - 0.9962]

teststem = [1.0 - 0.2100, 1.0 - 0.2116, 1.0 - 0.2308, 1.0 - 0.2394]
trainstem = [1.0 - 0.9810, 1.0 - 0.9685, 1.0 - 0.9502, 1.0 - 0.8886]

x = [1000, 2000, 5000, 10000]

plt.figure(1)
plt.subplot(211)

l1, l2 = plt.plot(x, train, x, test)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))
plt.title("Linear SVM Training vs. Test Set Error", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Error", fontsize = ftsz)

plt.subplot(212)
l1, l2 = plt.plot(x, trainstem, x, teststem)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)

ftsz = "xx-large"

plt.title("Linear SVM Training vs. Test Set Error (Stemmed words)", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Error", fontsize = ftsz)

save("linsvm_train_vs_test_both")
