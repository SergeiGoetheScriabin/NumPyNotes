import numpy as np
#Transposing and reshaping a matrix
    #This section covers arr.reshape(), arr.transpose(), arr.T

#It's common to need to transpose your matrices. NumPy arrays have the property T that allows you to transpose a matrix
    #useful image: https://numpy.org/doc/stable/_images/np_transposing_reshaping.png

#You may also need to switch the dimensions of a matrix.
    #This is where the reshape method can be useful. You simply need to pass in the new dimensions that you want for the matrix.
data = np.array([[1, 2], [3, 4], [5, 6]])
print(data.reshape(2, 3))
print(data.reshape(3, 2))
#Useful image: https://numpy.org/doc/stable/_images/np_reshape.png

#You can also .transpose() to reverse or change the axes of an array according to the values you specify
    #If you start with this array:
arr = np.arange(6).reshape((2, 3))
print(arr)
print(arr.transpose()) #arr.T also works as well.



