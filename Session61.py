"""
    PyTorch
    An Introduction to Torch Tensors (n-D Arrays)

    Reference Tutorials: https://pytorch.org/tutorials/

"""

import torch
print(torch.__version__)



A = torch.rand(5, 3)
print(A)
print(type(A)) # <class 'torch.Tensor'>

print()

B = torch.empty(5, 3)
print(B)

print()

# C = torch.zeros(5, 3)
# C = torch.zeros(5, 3, dtype=torch.int)
C = torch.zeros(5, 3, dtype=torch.long)
print(C)

print()

D = torch.tensor([10, 20, 30, 40, 50])
print(D)

print()

D = D.new_ones(5, 3, dtype=torch.double)
print(D)

print()

E = torch.rand_like(D, dtype=torch.float)
print(E)

print(E.size())
print(E.shape)

print()

X = torch.rand(5, 3)
Y = torch.rand(5, 3)

print(X)
print(Y)

# Z = torch.add(X, Y)
Z = X + Y
print(Z)

result = torch.empty(5, 3)
torch.add(X, Y, out=result)
print(result)


# Add X and Y and store result in X
X.add_(Y)
print(X)

# Slicing
print("X[:, 1]")
print(X[:, 1])  # 1st Column

