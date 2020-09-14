import pandas as pd

table1 = pd.read_csv("IPL-DATA-SET-2018.csv")
table2 = pd.read_csv("IPL-DATA-SET-2019.csv")

print(table1)
print(table2)

print("CONCATENATING ROW WISE")
# table3 = pd.concat([table1, table2])
table3 = pd.concat([table1, table2], axis=0)
print(table3)

print("CONCATENATING COLUMN WISE")
# table3 = pd.concat([table1, table2])
table4 = pd.concat([table1, table2], axis=1)
print(table4)

print("APPENDING TABLE IN TABLE")
table5 = table1.append(table2)
print(table5)