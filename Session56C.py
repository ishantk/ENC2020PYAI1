"""
    XOR

    A   B   Y
    0   0   0
    0   1   1
    1   0   1
    1   1   0

    Every Logical operation is done with the help of 3 gates
    AND OR and NOT :)

    A XOR B
    (A OR B) AND (NOT (A AND B))

    0 XOR 0
    -------
    (0 OR 0) AND (NOT (0 AND 0))
    0   AND (NOT (0) )
    0 AND 1
    0

    0 XOR 1
    -------
    (0 OR 1) AND (NOT (0 AND 1))
    1   AND (NOT(0))
    1 AND 1
    1

    1 XOR 0
    -------
    (1 OR 0) AND (NOT (1 AND 0))
    1   AND (NOT(0))
    1 AND 1
    1

    1 XOR 1
    -------
    (1 OR 1) AND (NOT (1 AND 1))
    1   AND (NOT(1))
    1 AND 0
    0


"""

# User Perceptrons from Session 56, 56A and write XOR with OOPS :)