# Software Solution for Some Snacks Point Shop :)

class FoodItem:

    def __init__(self, item_code, item_name, item_price, quantity):
        self.item_code = item_code
        self.item_name = item_name
        self.item_price = item_price
        self.quantity = quantity

    def get_food_item_details(self):
        return "{},{},{},{},{}\n".format(self.item_code, self.item_name, self.item_price, self.quantity, (self.quantity * self.item_price))

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

file = open("orders-11-8-2020.csv", "a")
file.write(customer_name)
file.write("\n")

while True:
    code = int(input("Enter Next Item Code: "))

    if code == 0:
        break

    quantity = int(input("Enter Item Quantity: "))

    item_data = FoodItem(code, items[code], prices[code], quantity)
    file.write(item_data.get_food_item_details())


print("ORDER PLACED & SAVED IN FILE :)")
