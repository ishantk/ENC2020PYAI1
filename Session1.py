# this is our session 1
"""
    Multi Line comment
    eg: JIO
	Mr. Ambani would like to know how much profits he made today ?

	100       | Profits
	25 -> 350 | 5.79    | 4G
	25 -> 1000| 55.22   | Wifi
	25 -> 2000| 101.99  | Phone
	25 -> 100 | 2.5     | Premium Customer

"""

# MODEL
# Creational Statements: to create Models i.e. Storage Containers in Memory
# Below containers are also known as variables as data in them may change
customers = 25
profits_4g = 5.79
profits_wifi = 55.22
profits_phone = 101.99
profits_premium = 2.5

# Update data in container
profits_4g = 5.88 # variable, value can be modified :)

# CONTROLLER
# Mathematical Computation
total_profits = (customers*profits_4g) + (customers*profits_wifi) + (customers*profits_phone) + (customers*profits_premium)

# VIEW
# Input or Output
# As of now we will display the total profits -> OUTPUT
print("TOTAL PROFITS:", total_profits)