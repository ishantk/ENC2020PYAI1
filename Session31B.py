import numpy as np

A = list(range(1, 11))
print(A)

X = np.arange(1, 11)
print(X)

# Compute the performance for above statements i.e. numpy vs list with time stamps :)

# Index Management
X[0] = 12
X[1] = 99

print(X)
print(X[7])

# deletion not possible
# del X[9]

print("SLICING")

# Slicing
print(X[2:6])   # 2 to 5
print(X[3:])    # 3 onwards
print(X[:5])    # 0 to 4

# Step Slicing
# [12 99  3  4  5  6  7  8  9 10]
print(X[1:7:2]) # [99 4 6]
print(X[1:7:3]) # [99 5] # form 1 to 6 with step of 3

# Negative Slicing
print(X[-5:9])  #[6 7 8 9]

# Boolean Slicing
print(X[X>5])

print()

# Slicing on Multi Dimensional Arrays
Y = np.array(
    [
       # 0  1
        [1, 2], # 0
        [3, 4], # 1
        [5, 6], # 2
    ]
)

print(Y)
print()
print(Y[0:2, 0:2])
print(Y[0:2, 1:2])
print()

# [0, 1, 2] -> represents the array in arrays
# [0, 0, 1] -> represents the elements of array in arrays
print(Y[[0, 1, 2], [0, 0, 1]]) # [1 3 6]
