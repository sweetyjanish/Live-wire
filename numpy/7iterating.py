import numpy as np

#iterating
#one by one.
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

#2D iterating
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)
  
for x in arr:
  for y in x:
    print(y)
    
#3D iterating    
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
    
for x in arr:
  for y in x:
    for z in y:
      print(z)

#nditer
for x in np.nditer(arr):
  print(x)
  
#Iterating Array With Different Data Types
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

#Step Size
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
  print(x)
  
#ndenumerate() 2D
for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
##ndenumerate() 1D
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
  print(idx, x)