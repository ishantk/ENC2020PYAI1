# SET | {}
# Uniqueness : List with uniquness

# john will always have the same hashcode if we want to store it in the memory
name1 = "john"
name2 = "john"

print(name1, type(name1), hex(id(name1)))
print(name2, type(name2), hex(id(name2)))

# Set is not Indexed
# Set is Hashed
followers = {"john", "jennie", "fionna", "mike", "leo"}
print("followers is:", followers)
print("Type of followers is:", type(followers))
print("followers hashcode is:", hex(id(followers)))

followers.add("sia")
followers.add("dave")
followers.add("fionna")
followers.add("john")

print("followers now:", followers)
print("Total Followers:", len(followers))

# we cannot access a single element from set
# we can add or remove
followers.remove("jennie")

print("followers now:", followers)
print("Total Followers:", len(followers))


# Set is Unordered in output
#     as data is stored not on indexes but with hashcodes
#     Set displays the data bucketwise

