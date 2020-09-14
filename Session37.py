"""
    Pandas in Continuation :)
    Part-II
"""

import pandas as pd

table1 = pd.read_csv("IPL-DATA-SET-2018.csv")
table2 = pd.read_csv("IPL-DATA-SET-2019.csv")

print(table1)
print(table2)

# For Reference Reading on Joins in SQL : https://www.w3schools.com/sql/sql_join_left.asp
# JOIN Operation :)
# give me all the records in left table i.e. table1 and show the matching records from the right table i.e. table2
table3 = pd.merge(table1, table2, on="TEAM", how="left")
# table3 = pd.merge(table1, table2, on="TEAM", how="right")
# table3 = pd.merge(table1, table2, on="TEAM", how="inner")
# table3 = pd.merge(table1, table2, on="TEAM", how="outer")

print(table3)
print(table3.YEAR_x)
print(table3.YEAR_y)