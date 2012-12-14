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
test = [1.0 - 0.2746, 1.0 - 0.2735, 1.0 - 0.2796]
train = [1.0 - 1.000, 1.0 - 0.9995, 1.0 - 0.9984]

x = [1000, 2000, 5000]

l1, l2 = plt.plot(x, train, x, test)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))

ftsz = "xx-large"

plt.title("Linear SVM Training vs. Test Set Error", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Error", fontsize = ftsz)

save("linsvm_train_vs_test")
