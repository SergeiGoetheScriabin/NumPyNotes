import numpy as np
#How to save and load NumPy objects
    #This section covers np.save, npsavez, np.savetxt, np.load, np.loadtxt
#The ndarray objects can be saved to and loaded from files with loadtxt and savetxt functinos.
        #load and save functions that handle NumPy binary files with a .npy file extension, and savez function that hundles NumPy files with a .npz file extension.
#The .npy and .npz files store data, shape, dtype, and other information required to reconstruct the ndarray in a way that allows the array to be correctly retrivied, even when the file is on another machine with different architecture.
#If you want to store a single ndarray object, store it as a .npy file using np.save .
    #If you want to store more than one use np.savez .
        #If you want to save several arrays use savez_compressed.
            #It's easy to save and load an array with np.save(). Just make sure to specify the array you want to save and a file name.
#For example, if you create this array:
a = np.array ([1, 2, 3, 4, 5, 6])
#you can save it as filename.npy with:
np.save('filename', a)
#You can use np.load() to reconstruct your array
b = np.load('filename.npy')

#To check your array, simply type: print(b)

#For example, let's say you create this array:
csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,])
#You can easily save it as a .csv file with the name "new_file.csv" like this
np.loadtxt('new_file.csv')

