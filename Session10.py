"""
    Set and Dictionary
"""

john_friends = {"fionna", "lee", "ben", "mike", "sia", "kim"}
jack_friends = {"dave", "ben", "kim", "harry"}
tim_friends = {"mike", "sia", "kim"}

# print(john_friends, type(john_friends))
print("john_friends")
print(john_friends)
print()

print("jack_friends")
print(jack_friends)
print()

print("tim_friends")
print(tim_friends)
print()

# S1 = john_friends | jack_friends # Union Operation
# S2 = john_friends & jack_friends # Intersection Operation
# S3 = john_friends - jack_friends # Difference Operation

S1 = john_friends.union(jack_friends) # Union Operation
S2 = john_friends.intersection(jack_friends)# Intersection Operation
S3 = john_friends.difference(jack_friends) # Difference Operation


print("S1 is:")
print(S1)
print()

print("S2 is:")
print(S2)
print()

print("S3 is:")
print(S3)
print()

# Membersip testing
print("fionna" in john_friends)
print("lee" not in tim_friends)

print(tim_friends.issubset(john_friends))
print(john_friends.issuperset(tim_friends))

# Explore more functions on Sets
# -> symmetric_difference