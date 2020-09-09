"""
    SeaBorn       ->    Data Visualization
        majorly for statistical graphics -> seaborn is preferred
        its built on top of matplotlib

        seaborn is integrated closely to pandas[data analysis library]
        seaborn provides data set oriented APIs

        pip install seaborn

        For Reference Reading: http://seaborn.pydata.org

"""

import matplotlib.pyplot as plt
import seaborn as sns

# Data-Set
tips = sns.load_dataset("tips")
print(tips)
print(type(tips)) # DataFrame from Pandas Library

penguins = sns.load_dataset("penguins")
print(penguins)
print(type(penguins))

# apply a default theme
sns.set_theme()

# Relational Plot
# sns.relplot(data=tips, x="total_bill", y="tip", style="smoker", hue="smoker", size="size", col="time")

# Linear Regression Plot
# sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time")

# Distribution Plot
# sns.displot(data=tips, x="total_bill", col="time", kde=True) # kde -> kernel density estimation

# Categorical Plot
# sns.catplot(data=tips, x="day", y="total_bill", hue="smoker", kind="swarm")
# sns.catplot(data=tips, x="day", y="total_bill", hue="smoker", kind="violin", split=True)

# sns.catplot(data=tips, x="day", y="total_bill", hue="smoker", kind="bar")

sns.pairplot(data=penguins, hue="species")

# Please explore more examples on Seaborn Library Documentation :)

plt.show()