import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#ndarray change tuples 
arrtuple= np.array((1, 2, 3, 4, 5))
print(arrtuple)

#0D array
arr = np.array(42)
print(arr)
print(arr.ndim)

#1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.ndim)

#2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)

#3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr.ndim)

#ndim
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

#access array element
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

#two dimension array element access
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])
print('5th element on 2nd row: ', arr[1, 4])

#three dimension array element access
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])