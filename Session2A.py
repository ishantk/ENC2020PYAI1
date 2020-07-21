"""
    Storage Containers in Memory
    With 4 Operations:
    1. Create
    2. Update
    3. Read
    4. Delete
"""

# 1. Create Operation
johns_age = 20
# 3. Read Operation
print(johns_age, type(johns_age), id(johns_age))

# johns_age is a reference variable
# 20 is the data i.e. literal
# 20 gets stored in the memory and has a HashCode
# reference variable johns_age will hold that HashCode

print()

# 1. Create Operation
leos_age = 20
print(leos_age, type(leos_age), id(leos_age))

print()

# 2. Update Operation
# In leos_age reference variable
leos_age = 26
print(leos_age, type(leos_age), id(leos_age))

print()

# Reference Copy| HashCode from RHS gets copied to LHS
# Copy Operation
kims_age = leos_age
print(kims_age, type(kims_age), id(kims_age))

# 4. Delete Operation
# del johns_age # johns_age and the corresponding data will be deleted
# print(johns_age, type(johns_age), id(johns_age)) # error

print()

del leos_age
# print(leos_age, type(leos_age), id(leos_age)) # error
print(kims_age, type(kims_age), id(kims_age))   # OK