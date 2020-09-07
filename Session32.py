"""
    numpy Part-III
    Introduction to matplotlib
"""

# Broadcasting:
#   An important term for Machine Learning
#   Mathematically we do some operations on different shaped arrays
#   eg: adding a vector to a 2d array :)

import numpy as np

# 2-D Array
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6]
])

print("X: ")
print(X)
print(X.shape)
print()


# 1-D Array
vector = np.array([1, 0, 1])
print("VECTOR: ")
print(vector)
print(vector.shape)
print()

# Kind of copy operation with no data
# random data will be in it
Y = np.empty_like(X)
print("Y: ")
print(Y)
print(Y.shape)
print()

print("Adding Vector to X and getting the result in Y")

for i in range(len(X)): # 0, 4 i.e. 0 1 2 and 3
    Y[i, :] = X[i, :] + vector

print("Y AFTER")
print(Y)
print(Y.shape)
print()


A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [2],
    [4],
    [6]
])

print(A, A.shape)
print(B, B.shape)
print()
C = A + B
print(C, C.shape)


# In Broadcasting we are working on different shapes to do some mathematical computations
