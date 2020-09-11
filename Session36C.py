import pandas as pd
import numpy as np

data = np.random.randn(5, 4)
print(data)
print(data.shape)

table = pd.DataFrame(data=data, columns=["COL1", "COL2", "COL3", "COL4"])
print(table)

print()
print("COLUMN2 Data")
print(table["COL2"])

print()
print("COLUMN3 Data")
print(table.COL3)

print()
print("Iterate in DataFrame - 1")
# iteritems() => Iterate Column Wise
for key, value in table.iteritems():
    print(key)      # Column Name
    print("~~~~~~~~~~")
    print(value)    # Column Data
    print()


print()
print("Iterate in DataFrame - 2")
# iterrows() => Iterate Row Wise
for key, value in table.iterrows():
    print(key)      # Row Index
    print("~~~~~~~~~~")
    print(value)    # Row Data
    print()

print()
print("Iterate in DataFrame - 3")
# itertuples() => Iterate in DataFrame as Tuples
for row in table.itertuples():
   print(row)
   print("~~~~~~~~~~~")

