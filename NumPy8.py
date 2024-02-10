import numpy as np
#Basic array operations
    #This section will cover: addition, subtraction, multiplication, division, and other useful array operations.

#Let's create two arrays. One named 'data' and One named 'ones'
data = np.array([1,2])       #np.array= [1,2]
ones = np.ones(2, dtype=int) #np.ones = [1,1]
#You can add these arrays together with the plus sign.
print(data + ones)

#It is inevitable we are going to do more than just addition
print(data - ones)
print(data * data)
print(data / data)

#Basic operations are simple with NumPy. If you want to find the sum of th elements in an array, you'd use sum(). This works for 1D arrays, 2D arrays, and arrays in higher dimensions.
a = np.array([1, 2, 3, 4])
print(a.sum())
#To add the rows or the columns in a 2D array, you would specify the axis.
    #If you start with this array:
b = np.array([[1, 1], [2, 2]])
#You can sum over the axis of rows with:
print(b.sum(axis=0))
#You can sum over the axis of columns with:
print(b.sum(axis=1))


#Broadcasting
    #There are times when you might want to carry out an operation between an array and a single number.
        #Here is how it is done.
datuh = np.array([1.0, 2.0])
print(datuh * 1.6)


