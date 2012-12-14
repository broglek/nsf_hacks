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
nbtest = [1.0 - 0.2864, 1.0 - 0.3121, 1.0 - 0.3312, 1.0 - 0.3310]
nbtrain = [1.0-0.6740, 1.0-0.6305, 1.0 - 0.5966, 1.0 - 0.5620]

nbteststem = [1.0-0.2390, 1.0-0.2217, 1.0-0.1852, 1.0-0.1690]
nbtrainstem = [1.0-0.6630, 1.0-0.5240, 1.0-0.3624, 1.0-0.2844]

sgdtest = [1.0 - 0.2358, 1.0 - 0.2478, 1.0 - 0.2829, 1.0 - 0.2857]
sgdtrain = [1.0-1.0, 1.0-0.9995, 1.0 - 0.9976, 1.0 - 0.9946]

sgdteststem = [1.0 - 0.1688, 1.0 - 0.1548, 1.0 - 0.1826, 1.0 - 0.1821]
sgdtrainstem = [1.0-0.8060, 1.0-0.5200, 1.0 - 0.4148, 1.0 - 0.4383]

x = [1000, 2000, 5000, 10000]

plt.figure(1)
plt.subplot(221)

l1, l2 = plt.plot(x, nbtrain, x, nbtest)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))
plt.title("Naive Bayes Training vs. Test Set Error", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Error")

plt.subplot(222)
l1, l2 = plt.plot(x, nbtrainstem, x, nbteststem)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)



plt.title("Naive Bayes Training vs. Test Set Error (Stemmed)", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Error")

plt.subplot(223)
l1, l2 = plt.plot(x, sgdtrain, x, sgdtest)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))



plt.title("SGD Training vs. Test Set Error", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Error")

plt.subplot(224)


l1, l2 = plt.plot(x, sgdtrainstem, x, sgdteststem)
plt.legend([l1,l2],["Training Error", "Test Error"], loc=4)
plt.ylim((-0.1,1.1))



plt.title("SGD Training vs. Test Set Error (Stemmed)", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Error")

save("other_train_vs_test_both")
