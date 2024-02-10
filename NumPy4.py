import numpy as np
#How to determine the shape and size of an array
    #This section covers: ndarray.ndim, ndarray.size, ndarray.shape
#Let's start with this array!
array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])
print(array_example)


print(array_example.ndim) #To find the dimensions
print(array_example.size) #To find the total number of elements in the array
print(array_example.shape)#To find the shape of your array


#how to reshape an array
a = np.arange(6)
print(a)

b = a.reshape(3,2)
print(b)

c = np.reshape(a, newshape=(1,6), order='C') # a = array to be reshaped
print(c)                                     # newshape = new shape you want
                                             #order:C means to read/write elements using C-like index order, F, for fortan-olike
