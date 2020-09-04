import numpy as np

array = np.arange(10, 51, 2)
print(array)

indexes = slice(1, 20, 2) # python slice function works both with lists and numpy array
print(indexes)

print(array[1:20])
print(array[1:20:2])
print(array[indexes])