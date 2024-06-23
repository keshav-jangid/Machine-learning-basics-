import numpy as np
array = np.identity(3)
print(array)




array2 = ([1,2,3,4],[5,6,7,8])
print(array2)

num_list = [1,2,3,4,5]
np.array(num_list)
print(np.array(num_list))
print(type(num_list))

print(np.identity(4))                                        # retuns identity matrix

print(np.eye(4,5))

print(np.eye(4,)*4) 

print(np.zeros((4,5)))                                       # returns zero matrix of 4,5
print(np.ones((4,5)))                                        # returns ones matrix of 4,5

print(np.arange(5))                                          # returns array of 5 numbers
num = np.arange(0,20,2)
print(type(num))                                             # returns array of numebers between 0 to 20 with difference of 2
print(np.linspace(10,20,3))                                  # generates 3 numbers between 10 to 20 with equal differnce
print(np.random.rand())                                      # generates an random number 
print(np.random.rand(4))                                     # generates four random numbers
print(np.random.rand(5,5))                                   # generates 5,5 matrix of random numbers

print(np.random.randint(8,45))                               # generates random interger between given range 


print(np.random.randint(100))
print(np.random.seed(10))                                      # generates same random number on every runtime 
                                                               # numbers for further random gereations 
print(np.random.randint(100))

