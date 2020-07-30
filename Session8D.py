# Dictionary is key/value pair
# keys can be any type and value can be any type

menu = {
    "burger": 100,
    "fires": 50,
    "noodles": 150,
    "pizza": 250,
    "samosa": 20
}

# Here we not have indexes which are auto numbered from 0 to n-1
# Keys they serve the purpose of indexing for us :)

# updated an existing key's value :)
menu["fires"] = 60
# a key will be created with value :)
menu["shake"] = 100

print("Menu:")
print(menu, type(menu), hex(id(menu)))

# Assignment: Explore and draw memory representation of Dictionary :)

print(menu["pizza"])

items = []
cart = []
choice = "yes"
total = 0

while choice == "yes":

    item = input("Enter Food Item")
    items.append(item)
    cart.append(menu[item])
    total += menu[item]

    choice = input("Enter more Items (yes/no): ")


if sum(cart) > 250:
    print("Complimentry Food Items Added")
    items.extend(["nuggets", "softy"])
    cart.extend([0, 0])


print(items)
print(cart)
# print("Amount to Pay", total)
print("Amount to Pay", sum(cart))

"""
    mini project:
    # open Zomato/Swiggy
    # represent menu of a restaurant in your program
    # let user enter items along with quantity for every item
    # at final checkout  ask user for a promo code and give the discounts
    # in case bill exceeds some amount, give some additional items as described above to the user
    
    # Expectation is to get a screen record of your working project in whatsapp group :)
    
"""

# PS: explore -> insert, remove and pop on the list :)

data = [10, 20, 30, 40, 50]
print(data, hex(id(data)))

data += [60, 70]            # extending the list
print(data, hex(id(data)))



