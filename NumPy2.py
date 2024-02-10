#how to create a basic array
#this file should cover: np.array(), np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace(),dtype

import numpy as np
a = np.array([1,2,3]) #will print a simple array of [1,2,3]
print(a)

b = np.zeros(4) #will print an array filled with (x) amount of 0's
print(b)

c = np.ones(3) #will print an array filled with (x) amount of 1's
print(c)

d = np.empty(2)
print(d) #number inside empty array may vary.

e = np.arange(4) #prints an array of a range of numbers
print(e)

f = np.arange(2,9,2) #prints an array of evenly spaced intervals: 2 = first number, 9 = last number, 2 = step size
print(f)

g = np.linspace(0,10, num=5) #creates an array with values that are spaces linearly on a specific interval
print(g)


h = np.ones(4, dtype=np.int64 # in numpy the default data type is floating point (np.float64) by using dtype you can specify which you want!
print(h)
