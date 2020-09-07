import numpy as np

X = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

Y = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(X)
print()
print(Y)

print()
v_stack = np.vstack((X, Y))
print(v_stack)

print()
h_stack = np.hstack((X, Y))
print(h_stack)