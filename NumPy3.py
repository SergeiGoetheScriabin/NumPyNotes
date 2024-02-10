import numpy as np
#Adding, removing, and sorting elements
#This section covers np.sort(), np.concatenate()


#Let's just say, we start with this array.
arr = np.array([2,1,5,3,7,4,7,8])
#You can quickly sort the numbers in ascending order with:
print(np.sort(arr))


#How to concatenate an array with NP
arr1 = np.array([[2, 4], [6, 8]])
arr2 = np.array([[3, 5], [7, 9]])
npc = np.concatenate((arr1, arr2), axis = 0)
print (npc)

