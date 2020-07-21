"""
    Data Representation

    Number Systems: (Explore online if unaware)
    binary      Base 2
        8
        base of 2
    Decimal 8 4 2 1
    Power   3 2 1 0
    Binary  1 0 0 0

    decimal     Base 10
        145
        5 * 10 pow 0 ->   5
        4 * 10 pow 1 ->  40
        1 * 10 pow 2 -> 100
                        ---
                        145
    octal       Base 8
    hexadecimal Base 16
"""

number = 8
print("number in decimal is:", number)
print("number in binary is:", bin(number))
print("number in octal is:", oct(number))
print("number in hexadecimal is:", hex(number))

print()

print("HashCode of number in decimal is:", id(number))
print("HashCode of number in binary is:", bin(id(number)))
print("HashCode of number in octal is:", oct(id(number)))
print("HashCode of number in hexadecimal is:", hex(id(number)))