ids = {"john.w", "fionna", "dave.h", "kia", "ana"}
print(ids, type(ids), hex(id(ids)))

# every element in set is stored as hashing algo i.e. hashtable
# we don't have indexes we have hashcodes for the stored data
# hence, indexing cannot work here :(

# enhanced for loop, which will read the data from set by taking
# hashcodes automatically in the background
for id in ids:
    print(id)

print(len(ids))
# for max min on Ascii: Ref: http://www.asciitable.com/
print(max(ids)) # on Ascii | kia -> k has 107
print(min(ids)) # on Ascii | ana -> a has 97

# print(sum(ids)) # sum works on numbers and not on strings