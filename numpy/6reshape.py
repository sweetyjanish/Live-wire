import numpy as np

#reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
newarr = arr.reshape(2, 3, 2)
print("reshaped",newarr)

#base
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)#base value
print(arr.reshape(2, 4))#reshaped value

#unknown 
#Note: We can not pass -1 to more than one dimension.
newarr = arr.reshape(2, 2, -1)
print("unknown",newarr)

#Flattening the arrays
#reshape(-1)
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)