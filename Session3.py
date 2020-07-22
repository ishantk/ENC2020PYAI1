"""
    Multi Value Containers | Data Structures :)
        1. Tuple
        2. List
        3. Set
        4. Dictionary
"""

# Single Value Container
# Ref Var will hold the HashCode of the storage container which has only 1 value :)
instagram_id = "auribises"
print("instagram_id is:", instagram_id)
print("Type of instagram_id is:", type(instagram_id))
print("instagram_id hashcode is:", hex(id(instagram_id)))

print()

# Multi Value Container
# Ref Var will hold the HashCode of the storage container which has only multiple values :)
# Tuple is Indexed
#               0         1        2        3       4
# followers = "john", "jennie", "fionna", "mike", "leo"
followers = ("john", "jennie", "fionna", "mike", "leo")


print("followers is:", followers)
print("Type of followers is:", type(followers))
print("followers hashcode is:", hex(id(followers)))


print(followers[0])
print(followers[4])

print("Total Followers:", len(followers))

# this wont work
# followers[1] = "jennie.watson"

# Jennie wish to unfollow -> hence, delete operation
# this wont work
# del followers[1]

# PS: tuple data structure will have elements which cannot be modified
#     i.e. READ-ONLY Operation
#     Tuple is IMMUTABLE

# When to use Tuple: When our data is fixed and is only for the display purpose