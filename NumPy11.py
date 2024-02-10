import numpy as np
from numpy.random import default_rng
#Generating random numbers
#The use of random number generation is an important part of the configuration and evaluation of many numerical and machine learning algorithms. Whether you need to randomly initialize weights in an artificial neural network, split data into random sets, or randomly shuffle your dataset, being able to generate random numbers (actually, repeatable pseudo-random numbers) is essential.


#With Generator.integers, you can generate random integers from low to high. You can set endpoint=True to make the high number inclusive.
    #Let's generate a 2x4 array of random integers between 0 and 4 with:
rng = default_rng()

x = rng.integers(5, size=(2, 4))
print(x)

print('_____________') #to break up the sections
#----
#How to get unique items and counts
    #you can find the unique elemnts in an array easily with np.unique.
#e.g.
a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
#you can use np.unique to print the unique values in your array
unique_values = np.unique(a)
print(unique_values)
#To get the indicies of the values, pass return_index argument in np.unique as well as your array
unique_values, indicies_list = np.unique(a, return_index=True)
print(indicies_list)
#You can pass the return_counts argument in np.unique() along with your array to get the frequency count of unique values in a NumPy array.
unique_values, occurence_count = np.unique(a, return_counts=True)
print(occurence_count)
a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
#you can find unique values with
unique_values = np.unique(a_2d)
print(unique_values)
#if the axis argument isn't passed, your 2d array will be flattened
    #if you want to get the unique rows or columns make sure to pass the axis argument.
        #To find the unique rows, specify axis=0 and for columns specify axis=1
unique_rows = np.unique(a_2d, axis=0)
print(unique_rows)
#To get the unique rows, index position, and occurence count, you can use...
unique_rows, indicies, occurrence_count = np.unique(a_2d, axis=0, return_counts=True, return_index=True)
print(unique_rows)
print(indicies)
print(occurrence_count)
