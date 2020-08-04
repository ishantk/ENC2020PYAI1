employee = {
    "eid": 101,
    "name": "John Watson",
    "designation": "Lead Engineer",
    "salary": 80000,
    "technology": "Python"
}

print(employee)
print(type(employee))
print(len(employee))
print(min(employee))        # Ascii based keys
print(max(employee))        # Ascii based keys

# Update Data in Dictionary
employee["salary"] = 97500

# delete key value pair
del employee["technology"]

print(employee)

print(employee["name"])

# keys = employee.keys()
# print(keys, type(keys))

keys = list(employee.keys())
print(keys, type(keys))

values = list(employee.values())
print(values)

# employee.clear()

# Slicing
# print(employee["name":"salary"]) # error : Not ok