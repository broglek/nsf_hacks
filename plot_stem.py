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
bayes = [23.90, 22.17, 18.52]
svm_lin = [21.00, 21.16, 23.07]
#svm_rbf = [25.34, 25.63, 26.27]
grad_desc = [16.88, 15.48, 18.26]

x = [1000, 2000, 5000]

l1, l2, l3, l4 = plt.plot(x, bayes, x, svm_lin, x, grad_desc)
plt.legend([l1,l2,l3,l4],["Naive Bayes", "Linear SVM", "Stochastic Gradient Descent"], loc=4)

ftsz = "xx-large"

plt.title("5-Fold Cross Validation Accuracy (With Stemming)", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Cross Validation Accuracy", fontsize = ftsz)

save("stem_no_10k")
