"""

    Hashing Algo | Hashtable
    divide data by size of bucket
    remainder -> is the bucket number in which you need to store the data

    hash(number) -> hashCode -> number % buckets
    where % means remainder

    Access Time is very less when data is stored using HashTables

    nearly all the languages will use hash table to store the data in the memory

    Containers in Memory

"""
# Python Convention of creating names is all lower case and _ for spaces
# johns_age = 20      # 7
# sias_age = 13       # 0
# joes_age = 26       # 0
# jennies_age = 10    # 10

# 1. Creational Statements: Creates Storage Containers in the Memory using Hashing Technique
# Numbered Data
johns_age = 20      # int   | direct division with bucket length

# Numbered Data
taxes = 18.5        # float | exploration -> how floating points are hashed ?

# Textual Data
name = 'John Watson' # str  | ASCII Addition and than division with bucket length

# In Python we have Storage Containers
# Majorly, Numbered or Textual

# print("johns_age is:", johns_age, type(johns_age), id(johns_age))
# print("taxes are:", taxes, type(taxes), id(taxes))
# print("name is:", name, type(name), id(name))

# Format Printing
print("johns_age is: {}. Type is: {}. HashCode is: {}".format(johns_age, type(johns_age), id(johns_age)))
print("taxes are: {}. Type is: {}. HashCode is: {}".format(taxes, type(taxes), id(taxes)))
print("name is: {}. Type is: {}. HashCode is: {}".format(name, type(name), id(name)))

