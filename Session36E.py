import pandas as pd

table = pd.read_csv("IPL-DATA-SET-2019.csv")
print(table)

print()
print(table.POINTS)

print("GROUPING THE DATA FROM TABLE")

# Groups from the DataSet
# grouped_table = table.groupby('POINTS')
# print(grouped_table) # DataFrameGroupBy Object
# print(grouped_table.groups)

grouped_table = table.groupby(['TEAM', 'POINTS'])
print(grouped_table.groups)

for team, grp in grouped_table:
    print(team)
    print(grp)


print("Fetch a SINGLE GROUP")
print(grouped_table.get_group(('Chennai Super Kings', 18)))

# Visualize the DataSet for every single team from last 5 years of IPL with matplotlib/seaborn :)