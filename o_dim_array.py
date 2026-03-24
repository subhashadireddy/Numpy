import numpy as np
array = np.array(['a','b','c'])
print(array.ndim)
print(array)

#2d array
array1 = np.array([[1,2,3],
                   [2,5,6],
                   [8,3,6]])
print(array1)
print(array1.ndim)


#3d array
array2 = np.array([[[1,2,3],[2,5,6],[8,3,6]],
                   [[1,2,3],[2,5,6],[8,3,6]],
                   [[1,2,3],[2,5,6],[8,3,6]]])
print(array2)
print(array2.ndim)


print(array1.shape)
print(array2.shape)

print(array2[0,0,0])#multiDimIndexing
print(array2[0,0,1])#faster then Chain Indexing 