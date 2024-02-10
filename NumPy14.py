import numpy as np
#Reshaping and flattening multidimensional arrays
    #This section will go over .flatten(), and ravel()
x = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12]])
#You can use flatten to flatten your 1D array
print(x.flatten())
#The key point to remember is: your new array won't change the parent array
a1 = x.flatten()
a1[0] = 99
print('Original Array: ', x)
print('New Array: ', a1)


a2 = x.ravel()
a2[0] = 98
print(x) # Original array
print(a2) # New Array
