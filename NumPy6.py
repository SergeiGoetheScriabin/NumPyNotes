import numpy as np
#Indexing and slicing arrays
    #You can index and slice NumPy arrays similarly to how you would slice a python list

data = np.array([1,2,3])
print(data[1]) #returns index 1
print(data[0:2])    #returns index 0-2
print(data[1:])         #returns index 1 to end of array
print(data[-2:])            #returns index -2, we are counting backwards here...


#https://numpy.org/doc/stable/_images/np_indexing.png <- helpful image to visualize

#------


a = np.array([[1 , 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#You can easily print all of the values in the array that are less than 5
print(a[a < 5])
#You can also select, for example, numbers that are equal to or greater than 5, and use that condition to index an array.
five_up = (a >= 5)
print(a[five_up])
#You can select elements that are divisible by 2:
divisible_by_2 = a[a%2==0]
print(divisible_by_2)
#Or you can select elements that satisfy two conditions using the & and | operators:
c = a[(a > 2) & (a < 11)]
print(c)
#It gets even better, you can make use of logical operators & and | in order to return boolean valus that specify whether or not the values in an array fulfill a certain condition
five_up = (a > 5) | (a == 5)
print(five_up)

#------

#You can also use np.nonzero() to select elements or indicies from an array.

#Let's start with this array

x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
#You can use np.nonzero() to print the indices of elements that are, for example less than 5:
y = np.nonzero(x < 5)
print(y)
#In the above example, a tuple of arrays was returned: one for each dimension. The first array represents the row indicies where these values are found, and for the second array represents the column indicies where the values are found.
#If you want to generate a list of coordinates where the elements exist, you can zip the arrays, iterate over the list of coordinates, and print them. e.g.
list_of_coordinates= list(zip(y[0], y[1]))
for coord in list_of_coordinates:
    print(coord)
#You can also use np.nonzero() to print the elements in an array that are less than 5 with:
print(x[y])
#If the element you're looking for doesn't exist in the array, then the returned array of indices will be empty. For example:
not_there = np.nonzero(x == 42)
print(not_there)
