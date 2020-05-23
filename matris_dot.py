import numpy as np

a = np.array([[1,2],
             [3,4],
             [5,6]])

b = np.array([[1,2],
             [3,4],
             [5,6]])

dot = np.dot(a,b.T)
print(dot)
