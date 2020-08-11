# Software Solution for Some Snacks Point Shop :)

# dictionary of item codes and item names
items = {
    101: "Paneer Tikka",
    201: "Noodles",
    301: "Sandwich",
    401: "Samosa",
    501: "Burger"
}

# dictionary of item codes and item prices
prices = {
    101: 300,
    201: 200,
    301: 150,
    401: 20,
    501: 60
}

customer_name = input("Please Enter Customer Name: ")
order_data = []  # list of lists :)

while True:
    code = int(input("Enter Next Item Code: "))

    if code == 0:
        break

    quantity = int(input("Enter Item Quantity: "))

    # an empty list
    item_data = []
    item_data.append(code)          # 0th index : code
    item_data.append(items[code])   # 1st index : name
    item_data.append(quantity)      # 2nd index : quantity
    item_data.append(prices[code]*quantity) # 3rd index: total price

    order_data.append(item_data)    # as many as items we will punch they will be added in a list order_data


file = open("orders.csv", "a")

file.write(customer_name)
file.write("\n")

print("Final Order Details For", customer_name)
print(order_data)

print("~~~~~~~~~~~~~~~~")

for order in order_data:
    print(order)
    file.write("{},{},{},{}\n".format(order[0], order[1], order[2], order[3]))

print("~~~~~~~~~~~~~~~~")

print("ORDER SAVED IN FILE :)")

# Assignment: Punch more orders by multiple customers
#             Finally, read this file to show the customer who has maximum order value and minimum value
#             Also find the customer who has placed maximum times the order

