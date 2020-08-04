state = {
    "active": 147018,
    "confirmed": 450196,
    "deaths": 15842,
    "updatedtime": "03/08/2020 21:53:33",
	"state": "Maharashtra"
}

# iterating key wise using enhanced for loop
for key in state:
    # print(key)
    # print(state[key])
    # print()
    print("{} | {}".format(key, state[key]))


print()

for value in state.values():
    print(value)

print()

# List of Tuples where each tuple contains key value pair
items = state.items()
print(items)

for item in items:
    print(item[0], item[1])

print()

for key, value in state.items():
    print(key, value)