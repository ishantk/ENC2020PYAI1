import pandas as pd

numbers1 = [10, 20, 30, 40, 50]
numbers2 = [11, 22, 33, 44, 55]

employee1 = {"name": "John", "age": 22, "salary": 30000}
employee2 = {"name": "Jennie", "age": 24, "salary": 40000}
employee3 = {"name": "Jim", "age": 26, "salary": 50000}
employee4 = {"name": "Jack", "age": 28, "salary": 60000}
employee5 = {"name": "Joe", "age": 30, "salary": 70000, "designation": "Manager"}


table1 = pd.DataFrame([numbers1, numbers2])
table2 = pd.DataFrame([employee1, employee2, employee3, employee4, employee5])

print("TABLE1")
print(table1)

print()

print("TABLE2")
print(table2)

print()

print("COLUMN WISE DATA")
# Accessing Data in DataFrame
print(table1[0])            # Column Wise Data
print(table2["name"])       # Column Wise Data

print()
print("ACCESS CELL DATA")
# Extract cell data in table
print(table1[1][1])
print(table2["salary"][1])

print()
print("SLICING")
# Slicing on DataFrame
print(table1[0:])       # Row Wise Slicing :)
print(table2[0:2])

print()
print("DELETING DATA")
# del table1[0] # deleting column wise
# print(table1)

# Delete Row or Column on the Basis of Axis API: drop
# axis -> 0 | ROW
# axis -> 1 | COLUMN

# Immutable operation i.e. generates a new DataFrame
# table = table1.drop(0, axis=1)
# print(table1)
# print(table)

# Mutable operation i.e. The same DataFrame will be dropped with column | inplace=True
table1.drop(0, axis=1, inplace=True)
print(table1)

print("UPDATE DATA IN DATAFRAME")
table1[1][1] = 111  # Update Single Value
table1[2] = 222     # Update Entire Column

table2["salary"] = 75700

print(table1)
print(table2)
