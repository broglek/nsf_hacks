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
bayes = [28.64, 31.21, 33.11, 33.10]
svm_lin = [27.46, 27.35, 27.96, 28.07]
#svm_rbf = [25.50, 26.05, 26.60]
grad_desc = [23.58, 24.78, 28.29, 28.57]

bayesstem = [23.90, 22.17, 18.52, 19.29]
svm_linstem = [21.00, 21.16, 23.07, 23.94]
#svm_rbf = [25.34, 25.63, 26.27]
grad_descstem = [16.88, 15.48, 18.26, 18.21]

ftsz = "xx-large"
x = [1000, 2000, 5000, 10000]

plt.figure(1)

plt.subplot(211)

l1, l2, l3 = plt.plot(x, bayes, x, svm_lin, x, grad_desc)
plt.legend([l1,l2,l3],["Naive Bayes", "Linear SVM", "Stochastic Gradient Descent"], loc=4)

plt.title("5-Fold Cross Validation Accuracy", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Cross Validation Accuracy")

plt.subplot(212)

l1, l2, l3 = plt.plot(x, bayesstem, x, svm_linstem, x, grad_descstem)
plt.legend([l1,l2,l3],["Naive Bayes", "Linear SVM", "Stochastic Gradient Descent"], loc=4)

plt.title("5-Fold Cross Validation Accuracy (Stemmed)", fontsize = ftsz)
plt.xlabel("Training Set Size")
plt.ylabel("Cross Validation Accuracy")


save("both_with_10k")
