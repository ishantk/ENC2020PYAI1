"""
HAS-A Relationship
    1 to 1
    1 to many

    Objects may be related to each other
    Why we relate them so as to solve the problem more effectively !

    Customer HAS-An Address | 1 to 1
    Teacher HAS Students    | 1 to many


    Use Case: Zomato
    HAS-A Relationship Mappings

    1. Identify the Objects:
    ------------------------
        write the attributes and relations

    Restaurant
        name, phone, address, description, ratings, menu
    Menu
        title, num_of_dishes, dishes
    Dish
        name, price, rating
    Customer
        name, phone, address, num_of_orders, cart, current_order
    Cart
        dishes
    Order
        customer, restaurant, dishes, total_price, date_time_stamp

"""

# 2. Write classes for the objects
# Start coding from the class which has no reference linking

class Dish:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    def show_dish(self):
        print("-------------------------------------")
        print("|  {}  |  {}  |  {}  |".format(self.name, self.price, self.rating))
        print("-------------------------------------")


class Menu:

    def __init__(self, title, num_of_dishes, dishes): # dishes will be referring to a List of Dish Objects
        self.title = title
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show_menu(self):
        print("^^^^^MENU^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.title, self.num_of_dishes))
        print("-------------------------------------")

        print("DISHES: ")
        for dish in self.dishes:
            dish.show_dish()


class Restaurant:

    def __init__(self, name, phone, address, description, ratings, menu):
        self.name = name
        self.phone = phone
        self.address = address
        self.description = description
        self.ratings = ratings
        self.menu = menu


    def show_restaurnat(self):
        print("^^^^^RESTAURANT^^^^^")
        print("-------------------------------------")
        print("|  {}  |  {}  |".format(self.name, self.phone))
        print("|  {}  |  {}  |".format(self.address, self.ratings))
        print(self.description)
        print("-------------------------------------")

        self.menu.show_menu()

    # Whenever object will be deleted from the memory del will be executed
    # acts as destructor
    def __del__(self):
        print("Restaurant Deleted:", self.name)



def main():

    # 3. From Classes Create the Real Objects

    """
    dish1 = Dish(name="Samosa", price=36, rating=4.5)
    dish2 = Dish(name="Chole Bhature", price=143, rating=4.6)
    dish3 = Dish(name="Paneer Pakoda", price=25, rating=4.5)
    dish4 = Dish(name="Burger", price=100, rating=3.5)
    dish5 = Dish(name="Sandwich", price=80, rating=4.2)

    dishes = [dish1, dish2, dish3, dish4, dish5]

    menu = Menu(title="Veg Indian Food", num_of_dishes=len(dishes), dishes=dishes) # dishes=dishes -> 1 to many

    restaurant = Restaurant(name="Gopal Sweets", phone="+91 99999 66666",
                            address="Sarabha Nagar", description="Mithai, Bakery, Indian, Chinese etc",
                            ratings=4.7, menu=menu) # menu=menu -> 1 to 1 relationship


    restaurant.show_restaurnat()
    """

    # Optimized the Memory by eliminating Reference Variables which may not be used
    restaurant = Restaurant(
                            name="Gopal Sweets",
                            phone="+91 99999 66666",
                            address="Sarabha Nagar",
                            description="Mithai, Bakery, Indian, Chinese etc",
                            ratings=4.7,
                            menu=Menu(
                                        title="Veg Indian Food",
                                        num_of_dishes=5,
                                        dishes=[
                                            Dish(name="Samosa", price=36, rating=4.5),
                                            Dish(name="Chole Bhature", price=143, rating=4.6),
                                            Dish(name="Paneer Pakoda", price=25, rating=4.5),
                                            Dish(name="Burger", price=100, rating=3.5),
                                            Dish(name="Sandwich", price=80, rating=4.2)
                                        ]
                                     )
                            )

    # restaurant.show_restaurnat()

    restaurant.menu.dishes[1].show_dish()


    # del restaurant
    # we dont generally delete the objects as they will be automatically deleted for us :)


if __name__ == '__main__':
    main()

# Assignment: Implement Customer, Cart and Order Objects and relate them with above code :)