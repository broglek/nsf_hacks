from scipy.sparse import *
import numpy as np

class ExampleData:
  def __init__(self, numRows, numColumns):
    self.Xdata = dok_matrix((numRows, numColumns))
    self.Ydata = np.zeros(numRows)
	
  def readDataVectorFile(self, filename):
    f = open(filename, 'r')
    keydict = {}
    count = 0
    for line in f:
      r,c,value = line.split(' ')
      if not r in keydict:
        keydict[r] = count
        count += 1
      self.Xdata[keydict[r], int(c)-1] = int(value)

  def readClassificationFile(self, filename):
    f = open(filename)
    keydict = {}
    count = 0
    for line in f:
      y,value = line.split(' ')
      if not y in keydict:
        keydict[y] = count
        count += 1
      self.Ydata[keydict[y]] = float(value)
	
  def getSingleExample(self, i):
    return (self.Xdata.getrow(i), self.Ydata[i])
	
