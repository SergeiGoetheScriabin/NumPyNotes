import numpy as np
#How to create an array from existing data
    #This section covers: slicing and indexing,np.vstack(), np.hstack(), np.hsplit(), (This is missing .view and .copy)

#Good news! You can easily create a new array from a section of an existing array.
    #Let's say you have this array
a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    #You can create a new array from a section of your array any time by specifying where you want to slice your array.
arr1 = a[3:8]
print(arr1)
#As you can see, you grabbed a section of your array from index position 3 through index position 8

#You can also stack two existing arrays, both vertically and horizontally.
    #Let's say we have to arrays named a1, and a2 respectively.
a1 = np.array([[1, 1],
               [2, 2]])

a2 = np.array([[3, 3],
               [4, 4]])
#vstack will stack them vertically
print(np.vstack((a1, a2)))
#hstack will stack them horizontally
print(np.hstack((a1, a2)))

#Using hspit, you can split an array into several smallar arrays. You can specify either the number of equally shaped arrays to return or the columns after which the division should occur.
    #Let's say we have this array:
x = np.arange(1, 25).reshape(2,12)
print(x)
#We can split this into three equally splt arrays using
np.hsplit(x,3)
#If you wanted to split your array after the third and fourth column, you'd run:
np.hsplit(x, (3,4))


