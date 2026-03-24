import numpy as np
rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)


fruits = np.array(["apple","banana","coconut"])
fruit = rng.choice(fruits)
print(fruit)