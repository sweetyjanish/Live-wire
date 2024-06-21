from scipy import io
import numpy as np

#create and save array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

#print
print("printaa",mydata)

#print vec 
print("vectoraa",mydata['vec'])

#squeeze for original
# Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)
print("squeeze",mydata['vec'])