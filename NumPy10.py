import numpy as np
#Creating matrices
    #You can pass Python lists of lists to create a 2D array or matrix


data = np.array([[1, 2], [3, 4], [5,6]])
print(data)
#useful image of matrix https://numpy.org/doc/stable/_images/np_create_matrix.png
print(data[0,1])
print(data[1:3])
print(data[0:2, 0])
#useful image of indices https://numpy.org/doc/stable/_images/np_matrix_indexing.png


#you can aggregate matrices the same way you aggregate vectors
print(data.max())
print(data.min())
print(data.sum())
#useful image pt.3 https://numpy.org/doc/stable/_images/np_matrix_aggregation.png

new_data = np.array([[1, 2], [5, 3], [4, 6]])
print(new_data)
print(new_data.max(axis=0))
print(new_data.max(axis=1))
#useful image https://numpy.org/doc/stable/_images/np_matrix_aggregation_row.png


x = np.array([[1, 2], [3, 4]])
ones = np.array([[1, 1], [1, 1]])
print(x + ones)
#useful image https://numpy.org/doc/stable/_images/np_matrix_arithmetic.png x  s s = data
 

y = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(y + ones_row)
#useful image https://numpy.org/doc/stable/_images/np_matrix_broadcasting.png y = data

np.ones((4, 3, 2))
print(np.ones) #numpy will print an array that is 4 total columns, 3 columns per array, and 2 long.


#there is many instances where we want NumPy to initialize the values of an array, this is where ones and zeros comes in... We also have the ability to print a random array.
npones = np.ones(3)
print(npones) #ones array of 3
npzeros = np.zeros(3)
print(npzeros) #zero filled array of 3
rng = np.random.default_rng() #simplest way to generate random numbers
print(rng.random(3))
#useful image https://numpy.org/doc/stable/_images/np_ones_zeros_random.png

#Lastly you can also use: ones(), zeros(), and random to create a 2d array if you give them a tuple describing dimensions  of the matrix
#np.ones((3, 2))
#array([[1., 1.],
#       [1., 1.],
#       [1., 1.]])
#np.zeros((3, 2))
#array([[0., 0.],
#       [0., 0.],
#       [0., 0.]])
#rng.random((3, 2)) 
#array([[0.01652764,s 0.81327024],
#       [0.91275558, 0.60663578],
#       [0.72949656, 0.54362499]])  # may vary#

#^ above output is included
#useful image: https://numpy.org/doc/stable/_images/np_ones_zeros_matrix.png
