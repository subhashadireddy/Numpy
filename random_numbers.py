import numpy as np 
ran = np.random.default_rng()
print(ran.integers(1,7))


print(ran.integers(1,100,3))  #1-100 range and i nned 3 numbers .. 
print(ran.integers(1,100,(3,2)))#3 rows,3cols



#to get the same results all the time set the seed to 1.
rand = np.random.default_rng(seed=1)
print(rand.integers(1,5,2))