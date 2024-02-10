import numpy as np
#How to reverse an array
    #this section covers np.flip()
        #Let's begin with this 1D array.

arr = np.array([1,2,3,4,5,6,7,8])
#You reverse it with
reversed_arr = np.flip(arr)
print('Reversed Array: ', reversed_arr)

#Now, let's reverse a 2D array.

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

#You can reverse the content in all of the rows and all of the columns with:

reverzed_arr = np.flip(arr_2d)
print('Reversed Array: ', reverzed_arr)

reverzed_arr_rows = np.flip(arr_2d, axis=0)
print(reverzed_arr_rows)

reverzed_arr_columns = np.flip(arr_2d, axis =1)
print(reverzed_arr_columns)

arr_2d[1] = np.flip(arr_2d[1])
print('The columns of index 1 will be flipped: ', arr_2d) #5,6,7,8 becomes 8,7,6,5


arr_2d[:,1] = np.flip(arr_2d[:,1])
print('This will change the columns at index 1:', arr_2d) #2,7,10 becomes #10,7,2
