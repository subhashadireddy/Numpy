import numpy as np 
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print("sum",np.sum(array))
print("mean:",np.mean(array))
print("variance:", np.var(array))
print("STdeviation",np.std(array))
print("MIN:",np.min(array))
print("MAX:",np.max(array))
print("position of min value:",np.argmin(array))
print("pos of max value:",np.argmax(array))