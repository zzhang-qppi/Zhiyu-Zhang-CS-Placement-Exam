import sys
import urllib.request
import numpy as np

url = sys.argv[1]
f = urllib.request.urlopen(url)
list = []
for line in f:
    line_as_array = np.array(line.split(), dtype="int64")
    list.append(line_as_array)
num_grid = np.array(list)
f.close()

def linear_mult(data):
    a = data[...,0:-3]
    b = data[...,1:-2]
    c = data[...,2:-1]
    d = data[...,3:]
    p = a*b*c*d
#    assert(p.shape[0] == data.shape[0])
#    assert(p.shape[1] == data.shape[1]-3)
    try:
        return np.max(p)
    except ValueError:
        return

def diagonal_mult(data):
    a = data[0:-3,0:-3]
    b = data[1:-2,1:-2]
    c = data[2:-1,2:-1]
    d = data[3:,3:]
    p = a*b*c*d
#    assert(p.shape[0] == data.shape[0]-3)
#    assert(p.shape[1] == data.shape[1]-3)
    try:
        return np.max(p)
    except ValueError:
        return

try:
    print(max(list(filter(None, 
        [
            linear_mult(num_grid),
            linear_mult(num_grid.T[::-1]),
            diagonal_mult(num_grid),
            diagonal_mult(num_grid.T[::-1]),
        ]
        ))))
except ValueError:
    print("Your input contains no quadsequences.")

            