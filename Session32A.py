"""
    DOT PRODUCT

    M1
    [a  b]
    [c  d]

    M2
    [e  f]
    [g  h]

    M3
    [ae+bg  af+bh]
    [ce+dg  cf+dh]

"""

import numpy as np

matrix1 = np.array([
    [2, 3],
    [1, 4]
])

matrix2 = np.array([
    [2, 3],
    [1, 6]
])

matrix3 = np.dot(matrix1, matrix2)
print(matrix3)


matrix1_det = np.linalg.det(matrix1)
print(matrix1_det)

"""
explore more:
    np.linalg.det()
    np.linalg.inv()
    np.linalg.norm()
    .
    ..
    ....
"""

# PS: numpy almost contains all the mathematical functions for matrices :)
