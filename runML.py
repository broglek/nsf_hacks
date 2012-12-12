#!/usr/bin/env python
# encoding: utf-8

from read_Matrix import ExampleData
from scilearn import Learner
from sklearn import cross_validation
import numpy as np
from scipy.sparse import *

data = ExampleData(2000, 30799)
data.readDataVectorFile('docwords_master_2000')
data.readClassificationFile('ids_and_amounts_2000')

avgNB = 0
avgLin = 0
numTrials = 5
for n in range(numTrials):
 
    learner = Learner(None)
    score = learner.test_kf("NB", data.Xdata, data.Ydata)
    meanNB = score.mean()
    avgNB += meanNB
    print "NB:", meanNB
    lin = Learner(None)
    score = lin.test_kf("LinearSVC", data.Xdata, data.Ydata)
    meanLin = score.mean()
    avgLin +=  meanLin
    print "LinearSVC:", meanLin
    
avgNB /= numTrials
avgLin /=numTrials
print "NB Avg:%f\tLinearSVC Avg:%f" %(avgNB, avgLin)