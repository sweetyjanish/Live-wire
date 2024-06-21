import numpy as np

#print no of rows and columns
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#print no of rows and columns
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)