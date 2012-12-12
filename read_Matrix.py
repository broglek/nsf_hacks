from scipy.sparse import *
import numpy as np

class ExampleData:
  def __init__(self, numRows, numColumns):
    self.Xdata = dok_matrix((numRows, numColumns))
    self.Ydata = np.zeros(numRows)
	
  def readDataVectorFile(self, filename):
    f = open(filename, 'r')
    for line in f:
      r,c,value = line.split(' ')
      self.Xdata[int(r)-1, int(c)-1] = int(value)

  def readClassificationFile(self, filename):
    f = open(filename)
    for line in f:
      y,value = line.split(' ')
      self.Ydata[int(y)-1] = float(value)
	
  def getSingleExample(self, i):
    return (self.Xdata.getrow(i), self.Ydata[i])
	
