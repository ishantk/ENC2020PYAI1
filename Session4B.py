# Bitwise Operators
#  & | ^

# Shift Operators
# >>, <<

# they are majorly in Cyber Security, Networking, Gaming

num1 = 12
num2 = 4

print(bin(num1))    # 1 1 0 0
print(bin(num2))    # 0 1 0 0

num3 = num1 & num2  # 0 1 0 0
print(num3, bin(num3))

num4 = num1 ^ num2  # 1 0 0 0
print(num4, bin(num4))

print(num1, num2)

# Bitwise XOR: Swapped the data in the containers :)
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(num1, num2)

# in a multi value container, we can try finding some integer that wont appear twice
# in a game like pub g, user will have players location movements from one point to another
# point is (x, y) -> changes in the locations can be managed through shift operators

num1 = 12
num6 = num1 >> 2
# 1 1 0 0 >> 2
# _ _ 1 1
# 0 0 1 1 -> 3

# number divisible by 2 power shift | 12 // 2pow2

print(num6, bin(num6))

num7 = num1 << 2
# 1 1 0 0 << 2
# 1 1 0 0 _ _
# 1 1 0 0 0 0

# number multiplied by 2 power shift | 12 * 2pow2
print(num7, bin(num7))


data = 8     # information to be passed
key = 2      # is available at both sender and receiver

# sender sends the information
sent_info = data >> key
print("Information Sent:", sent_info)

# receiver receives the information
received_info = sent_info << key
print("Information Received:", received_info)

# Assignment:
# Explore shift operators on negative numbers
# hint -> 1s and 2s complement

