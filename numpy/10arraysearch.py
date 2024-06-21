import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

#even
x = np.where(arr%2 == 0)
print(x)

#odd
x = np.where(arr%2 == 1)
print(x)

#position
x = np.searchsorted(arr, 6)
print("pos",x)

#right side of value
x = np.searchsorted(arr, 5, side='right')
print(x)

# ARRAY PLACE
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)