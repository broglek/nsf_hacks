#!/usr/bin/env python
# encoding: utf-8

from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn import cross_validation
from numpy import shape

class Learner:
  def __init__(self, data):
    #data is an ExampleData class that has already read in the
    #data vectors and classifications
    self.data = data
    
    #Create a dictionary of different classifiers
    self.clf = dict()
    self.clf["SGD"] = SGDClassifier(loss="hinge", penalty="l2", n_iter=100, shuffle=True)
    self.clf["SVM"] = svm.SVC()
    self.clf["LinearSVC"] = svm.LinearSVC()
    self.clf["NB"] = MultinomialNB()
    
    #Create a dictionary of "results" for each classifier
    #Each result is itself a dictionary of how many misclassified
    self.results = dict()
  
  '''
  Train the classifier specified by "classifier"
  '''
  def learn(self, classifier):
    self.clf[classifier].fit(self.data.Xdata, self.data.Ydata)
  
  '''
  Test the classifier specified by "classifier" by using
  kfold cross-validation. 
  '''
  def test(self, classifier, testData, testTargets):
    correct = 0.0
    total = 0.0
    results = dict()
    
    for i in range(len(testTargets)):
      predicted = self.predict(testData.getrow(i), classifier)
      if predicted == testTargets[i]:
        correct += 1.0
      else:
        if testTargets[i] in results.keys():
          results[testTargets[i]] += 1.0
        else:
          results[testTargets[i]] = 0.0
      total += 1.0
    self.results = results
    return correct / total
  
  
  def test_kf(self, classifier, testData, testTargets):
    ndim = shape(testData)
    kf = cross_validation.KFold(ndim[0], k=5, shuffle = True)
    scores = cross_validation.cross_val_score(self.clf[classifier], testData, testTargets, cv=kf)
    return scores
  '''
  Predict the classification of feature vector x using "classifier"
  '''
  def predict(self, x, classifier):
    return self.clf[classifier].predict(x)

