"""
    NUMPY - Part 2
"""

import numpy as np

array1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(array1)
print(array1.shape) # (2, 3)
print(array1.shape[0]) # 2
print(array1.shape[1]) # 3

print("Re-Shaping Array")

array2 = array1.reshape(3, 2)
print(array1)
print(array1.shape)
print()
print(array2)
print(array2.shape)

print()

array_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [1, 2, 3],
        [4, 5, 6]
    ]
])

print(array_3d)
print(array_3d.shape)

# Assignment: try reshaping the 3d array
# PS: reshaping must be done correctly :)