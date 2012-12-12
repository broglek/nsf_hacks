#!/usr/bin/env python
# encoding: utf-8

from read_Matrix import ExampleData
from scilearn import Learner
from sklearn import cross_validation
import numpy as np
from scipy.sparse import *
import sys
import getopt



def runML(dataFile, classFile, vocab, samples):
    print "Samples:" , samples
    print "Vocab size:", vocab
    data = ExampleData(int(samples), int(vocab))
    data.readDataVectorFile(dataFile)
    data.readClassificationFile(classFile)
    avgNB = 0
    avgLin = 0
    avgSVC = 0
    avgSGD = 0
    numTrials = 5
    learner = Learner(None)
    for n in range(numTrials):
     
        
        score = learner.test_kf("NB", data.Xdata, data.Ydata)
        meanNB = score.mean()
        avgNB += meanNB
        print "NB:", meanNB
        score = learner.test_kf("LinearSVC", data.Xdata, data.Ydata)
        meanLin = score.mean()
        avgLin +=  meanLin
        print "LinearSVC:", meanLin
        score = learner.test_kf("SGD", data.Xdata, data.Ydata)
        meanSGD = score.mean()
        avgSGD +=  meanSGD
        print "SGD:", meanSGD
        score = learner.test_kf("SVM", data.Xdata, data.Ydata)
        meanSVC = score.mean()
        avgSVC +=  meanSVC
        print "SVM:", meanSVC
        
        
    avgNB /= numTrials
    avgLin /=numTrials
    avgSGD /=numTrials
    avgSVC /=numTrials
    print "NB Avg:%f\tLinearSVC Avg:%f\tSVM Avg:%f\tSGD Avg:%f" %(avgNB, avgLin, avgSVC, avgSGD)
    
class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg
 # takes in -d datafile -c classfile -v vocabsize -s #samples
# example python runML.py -d docwords_master_1000 -c ids_and_amounts_1000 -v 30799 -s 1000 
def main(argv=None):
    samples = 0
    vocab = 0
    datafile = ''
    classfile = ''
    if argv is None:
        argv = sys.argv
        if len(sys.argv) <2:
            Usage("Not enough args")
            sys.exit()
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hs:v:d:c:", ["help"])
            for o, arg in opts:
                if o in ("h", "--help"):
                    usage()
                    sys.exit()
                elif o in ("-s"):
                    samples = arg
                elif o in ("-v"):
                    vocab  = arg
                elif o in ("-d"):
                    datafile = arg
                elif o in ("-c"):
                    classfile = arg
                    
        except getopt.error, msg:
             raise Usage(msg)
        runML(datafile, classfile, vocab, samples)
    except Usage, err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2

if __name__ == "__main__":
    sys.exit(main())