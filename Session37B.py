"""
    Soccer DataSet Analysis
    Objective : Finding the Best Goalkeepers :)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

table = pd.read_csv("soccerdata.csv")
print(table)

print("First5 Records")
print(table.head())

print("Last5 Records")
print(table.tail())

print("Names:")
# print(table.Name)
print(table['Name'])


# sns.countplot(y=table.Nationality, palette="Set2")
# sns.countplot(x="Age", data=table)
# sns.countplot(x="Nationality", data=table)

# Explore -> Format Country Names Diagonally on the seaborn :)
# names may come as diagonal -> / / / / / / /

# plt.show()

"""
    We need to find the best goal keepers of the world -> who can stop the goals
    extract the attributes of a soccer player which are necessary for a GoalKeeper
    give them some weights as per the requirements
"""
# More weight means more importance

weight_positioning = 1
weight_diving = 2
weight_handling = 3
weight_reflexes = 4

# Add a new column in table
table["GK_SCORE"] = weight_positioning*table.GK_Positioning + weight_diving*table.GK_Diving + weight_handling*table.GK_Handling + weight_reflexes*table.GK_Reflexes

print(table)

print()

# Sort the Table on GK_SCORE Column
sorted_table = table.sort_values("GK_SCORE")
print(sorted_table)

print("LAST 10 Records are the Top 10 GoalKeepers")
print(sorted_table.tail(10))

# Pandas: Data Analysis Mini Project
# Analysze Cricketers with the similar algo as used above by webscrapping the data from espncricinfo website
# TOP 10 BatsMen and Bowlers :)