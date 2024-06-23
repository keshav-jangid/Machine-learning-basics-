import numpy as np

# ONE Dimensional Array 


array1 = np.array([1,2,3,4,5])


#psoitive indexing and Slicing

print(array1[2])
print(array1[1:4])
print(array1[:4])
print(array1[2:])
print(array1[0::2])

#negative indexing and Slicing
print(array1[-2])



# TWO Dimensional Array


array2 = np.array([[1,2,3,4],[5,6,7,8]])


# indexing and slicing of 2D array 

print(array2[1][2])                            # returns on element 
print(array2[1:])                              # returns complete row
print(array2[1])                                 # returns complete row

print(array2[:,1])                             # returns complete column

print(array2[:2,:2])                           # returns 2 rows snd 2 columns

