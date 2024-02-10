import numpy as np
#How to convert a 1D array into a 2D array (how to add a new axis to an array)
    #This section covers: np.newaxis, np.expand_dims



#you can use np.newaxis to add new axis to array
#using np.newaxis will increase the dimensions of your array by one dimension when used once  1D -> 2D -> 3D and so on

#Let's start with this array
a = np.array([1,2,3,4,5,6])
print(a.shape)

a2 = a[np.newaxis, :]
print(a2.shape)


row_vector = a[np.newaxis, :]
print(row_vector.shape)


col_vector = a[:, np.newaxis]
print(col_vector.shape)

#You can also expand an array by inserting a new axis at a specified position with np.expand_dims
#Let's start with this array
b = np.array([2,4,6,8,10])
print(b.shape)
#You can use np.expand_dims to add an index position 1 with
b = np.expand_dims(a, axis =1)
print(b.shape)
#You can add an axis at index position 0 with:
c = np.expand_dims(a,axis=0)
print(c.shape)
