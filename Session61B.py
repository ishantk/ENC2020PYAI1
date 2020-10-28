"""
    PyTorch and Numpy
    Bridiging between pytorch and numpy

"""

import numpy as np
import torch

X = torch.ones(5)
print(X, type(X))

print()

Y = X.numpy()
print(Y, type(Y))

X.add_(1)

print(X) # Manipulating tensor will also manipulate its numpy copy :)
print(Y)


print("``````````````")
A = np.ones(5)
B = torch.from_numpy(A)

print(A, type(A))
print(B, type(B))

np.add(A, 1, out=A) # Manipulating of numpy array manipulate its tensor copy :)

print(A)
print(B)