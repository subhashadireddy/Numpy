import numpy as np
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
#array[start:end:step]
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[-1])


print(array[0:4])
print(array[0:3])#ending index is excluded
print(array[::2])

#accessing cols------working on cols 
print(array[:,0])
print(array[:,1])
print(array[:,-1])#last column

#slicing cols
print(array[:,0:3])#prints col 0,1,2




# accesing both row and col at a time : 
print(array[0:2 , 0:2])#[row,col]