# Arithmetic Operations on numpy array

import numpy as np
A = np.array([
    [1, 2],
    [3, 4],
])

B = np.array([
    [5, 6],
    [7, 8],
])

print("A: ")
print(A)
print(A.shape)

print("B: ")
print(B)
print(B.shape)

print("SUM: ")
SUM = A + B
print(SUM)
print(SUM.shape)

print("DIFF: ")
DIFF = A - B
print(DIFF)
print(DIFF.shape)

print("MUL: ")
MUL = A * B
print(MUL)
print(MUL.shape)

print("DIV: ")
# DIV = A // B
DIV = A / B
print(DIV)
print(DIV.shape)

# Assignment: Explore where in the world of CS we need matrix arithmetic operations -> WhatsApp Chat Group

C = A + 5
D = B * 2
print("C: ")
print(C)

print("D: ")
print(D)

print()
E = np.sqrt(A)
print("E: ")
print(E)

print()
F = np.exp(A)
print("F: ")
print(F)


