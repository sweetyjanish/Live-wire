import numpy as np

#slicing particular index value
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#slicing thro end
print(arr[4:])

#slicing from begining
print(arr[:4])

#Negative Slicing
print(arr[-3:-1])

#STEP2
print(arr[1:5:2])

#begining to end step1
print(arr[::])

#begining to end step2
print(arr[::2])

#Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])
print(arr[0, 1:4])

#particular index value from both rows
print(arr[0:2, 3])
print(arr[0:1, 3])

#number of rows&index postions
print(arr[0:2, 1:4])
print(arr[0:1, 1:4])