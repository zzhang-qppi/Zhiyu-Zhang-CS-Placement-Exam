import sys
import urllib.request
import numpy as np

#url = sys.agrv[1]
url = "http://cs.carleton.edu/faculty/dln/placement/grid.txt"
f = urllib.request.urlopen(url)
list = []
for line in f:
    line_as_array = np.array(line.split(), dtype="int64")
    list.append(line_as_array)
data = np.array(list)
f.close()
