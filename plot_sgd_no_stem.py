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
test = [1.0 - 0.2358, 1.0 - 0.2478, 1.0 - 0.2829, 1.0 - 0.2857]
train = [1.0-1.0, 1.0-0.9995, 1.0 - 0.9976, 1.0 - 0.9946]

x = [1000, 2000, 5000, 10000]

l1, l2 = plt.plot(x, train, x, test)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))

ftsz = "xx-large"

plt.title("Stochastic Gradient Descent Training vs. Test Set Error", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Error", fontsize = ftsz)

save("sgd_train_vs_test")
