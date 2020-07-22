# List : [] | MUTABLE MVC
# also indexed:
#               0        1         2        3      4
followers = ["john", "jennie", "fionna", "mike", "leo"]

print("followers is:", followers)
print("Type of followers is:", type(followers))
print("followers hashcode is:", hex(id(followers)))

# List is MUTABLE i.e. we can perform manipulations in the list
followers.append("kia")
followers.append("dave")

print("followers now:", followers)

del followers[1]

print("followers now:", followers) # indexing will automatically be shifted
print(followers[1])

followers[1] = "fionna.flynn"

print("followers now:", followers)

# Challenge with List
# It supports duplicates

followers.append("george")
followers.append("harry")
followers.append("mike")    # duplicate
followers.append("john")    # duplicate

print("followers:", followers)
print("Total Followers:", len(followers))


