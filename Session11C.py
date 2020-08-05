"""
    Principle of OOPS
    1. Think of object
    2. Create its class
    3. From class, create real objects in memory

"""

# 1. Think of object
#    FoodItem : name, price, quantity

# 2. Create its class
class FoodItem:

    # attributes of class FoodItem as Storage Container. Not of Objects
    food_item_count = 0
    total_quantity = 0

    def __init__(self, name, price, quantity):
        # LHS self.name is an attribute which gets created in our object
        # RHS self.name is the input to the Constructor whose value is written in the attribute of object
        FoodItem.food_item_count += 1
        self.name = name
        self.price = price
        self.quantity = quantity

    def increment(self):
        FoodItem.total_quantity += 1
        self.quantity += 1

    def decrement(self):
        FoodItem.total_quantity -= 1
        self.quantity -= 1

    def show_food_item(self):
        print()
        print("---------------------------")
        print("FoodItem: {} | {}".format(self.name, self.price))
        print("Quantity: {}".format(self.quantity))
        print("----------------------------")

    def show(self):
        print("Total Food Items:", FoodItem.food_item_count)
        print("Total Quantity:", FoodItem.total_quantity)


def main():
    item1 = FoodItem("Burger", 200, 1)  # Object Construction
    item2 = FoodItem("Sandwich", 100, 1)  # Object Construction
    item3 = item1       # Reference Copy

    # How many objects have we created here ? A: 2
    # Will the above code work ? No, as for above objects we have not passed the inputs to constructor

    item1.show_food_item()
    item2.show_food_item()
    item3.show_food_item()

    item1.increment()   # i1/i3: 2
    item2.increment()   # i2: 2
    item3.increment()   # i1/i3: 3

    item1.increment()   # i1/i3: 4
    item2.increment()   # i2: 3

    item3.decrement()   # i1/i3: 3
    item1.decrement()   # i1/i3: 2

    item1.show_food_item()  # 2
    item2.show_food_item()  # 3
    item3.show_food_item()  # 2

    # How many different food items are thr ?   2
    # How many total quantity ?                 5 # Write/Rectify the Logic :)

    print()
    print("FoodItem Class Details:", FoodItem.__dict__)
    print("item1 Object's Details:", item1.__dict__)
    print("item2 Object's Details:", item2.__dict__)


    print()
    item1.show()
    item2.show()
    item3.show()

if __name__ == '__main__':
    main()

