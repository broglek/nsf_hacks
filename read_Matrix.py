from scipy.sparse import *
import numpy as np

class ExampleData:
  def __init__(self, numRows, numColumns):
    self.Xdata = dok_matrix((numRows, numColumns))
	self.Ydata = np.zeros(numRows)
	
  def readDataVectorFile(self, filename):
    f = open(filename, 'r')
    for line in f:
	  ff = line.split(' ')
	  self.Xdata[int(ff[0])-1, int(ff[1])-1] = int(ff[2])

  def readClassificationFile(self, filename):
    f = open(filename)
	for line in f:
	  ff = line.split(' ')
	  self.Ydata[int(ff[0])-1] = int(ff[1])
	
  def getSingleExample(self, i):
    return (self.Xdata.getrow(i), self.Ydata[i])
	
