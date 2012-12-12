#!/usr/bin/env python
# encoding: utf-8

from read_Matrix import ExampleData
from scilearn import Learner
from sklearn import cross_validation

data = ExampleData(2000, 30799)
data.readDataVectorFile('docwords_master_2000')
data.readClassificationFile('ids_and_amounts_2000')

for n in range(5):
  X_train, X_test, y_train, y_test = cross_validation.train_test_split(data.Xdata, data.Ydata, test_size=0.25, random_state=n, dtype=int)
  
  data_train = ExampleData(1500, 30799)
  
  data_train.Xdata = X_train
  data_train.Ydata = y_train
  
  learner = Learner(data_train)
  learner.learn("NB")
  score = learner.test("NB", X_test, y_test)
  print score
