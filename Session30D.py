import numpy as np

numbers = [1, 1, 1, 1, 1, 1, 1, 1]
array1 = np.array(numbers)
array2 = np.ones(8)
array3 = np.zeros(8)

print(array1)
print(array2)
print(array3)

# Assignment: Compare will shape printing take more time or len printing will take more time
print(array1.shape)
print(array2.shape)
print(array3.shape)

print(len(array1))
print(len(array2))
print(len(array3))


array = array1.reshape(2, 2, 2)
print(array)
print(array.shape)

# ravel -> bringing the array back to its original shape
array = array.ravel()
print(array)
print(array.shape)