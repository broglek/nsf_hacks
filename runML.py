#!/usr/bin/env python
# encoding: utf-8

from read_Matrix import ExampleData
from scilearn import Learner

data = ExampleData(2000, 30799)
data.readDataVectorFile('docwords_master_2000')
data.readClassificationFile('ids_and_amounts_2000')

learner = Learner(data)
learner.test("NB")
