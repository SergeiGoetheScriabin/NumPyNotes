import numpy as np
#More useful array operations
    #This section covers maximum, minimum, sum, mean, product, stdev, and more!

#NumPy also performs aggregation functions. In addition to min, max, and sum, you can easily run mean to get the average, prod to get the result of multiplying the elements together, std to get the standard deviation, and more.

data = np.array([1.0, 2.0])
print(data.max())
print(data.min())
print(data.sum())
#-----

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
print(a)#prints above array
print(a.sum())#prints the sum of array
print(a.min())#prints the lowest number of unsorted array
print(a.min(axis=0))#print botom axis The four values listed above correspond to the number of columns in your array. With a four-column array, you will get four values as your result.



