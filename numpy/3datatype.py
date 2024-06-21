import numpy as np

#checking datatype
arr = np.array([1, 2, 3, 4])
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

#create desire datatype
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#4byte integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#create excisting array datatype
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
#using int
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#boolean type
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)