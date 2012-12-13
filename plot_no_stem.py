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
bayes = [28.64, 31.21, 33.11]
svm_lin = [27.46, 27.35, 27.96]
svm_rbf = [25.50, 26.05, 26.60]
grad_desc = [23.58, 24.78, 28.29]

x = [1000, 2000, 5000]

l1, l2, l3, l4 = plt.plot(x, bayes, x, svm_lin, x, svm_rbf, x, grad_desc)
plt.legend([l1,l2,l3,l4],["Naive Bayes", "Linear SVM", "SVM with RBF Kernel", "Stochastic Gradient Descent"], loc=4)

ftsz = "xx-large"

plt.title("5-Fold Cross Validation Accuracy", fontsize = ftsz)
plt.xlabel("Training Set Size", fontsize = ftsz)
plt.ylabel("Cross Validation Accuracy", fontsize = ftsz)

save("no_stem_no_10k")
