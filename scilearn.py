#!/usr/bin/env python
# encoding: utf-8

from sklearn.linear_model import SGDClassifier
from sklearn import svm
from sklearn.naive_bayes import MultinomialNB
from sklearn import cross_validation

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
  def test(self, classifier, k=4):
    scores = cross_validation.cross_val_score(self.clf[classifier],
      self.data.Xdata, self.data.Ydata, cv=k)
    print scores
  
  '''
  Predict the classification of feature vector x using "classifier"
  '''
  def predict(self, x, classifier):
    return self.clf[classifier].predict(x)

