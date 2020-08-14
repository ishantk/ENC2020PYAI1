"""
    Persistence
    Google Firebase Firestore DB | very much same like the Mongo DB
    Data in Cloud :)

    SQL and NoSQL DB's

    Firestore DB works in a way we store data on our system i.e computer
    Databases is a collection of folders and files

    table -> collection
    document -> record / row

    Firestore Saves Documents and Collections
    Every Document will have a unique id in Collection
    Document Stores the data as a Dictionary :)
    Dictionary: i.e. key value pair
        dictionary key can also be a dictionary or a list

    DB Stores the data as
        collection
            /document1
                data
                    /collection
                        document1
                        document2
                        .
                        ..
                        ...
            /document2
                data


    Restaurant
        name, phone, email, ratings, operating_hours, address, dishes


    Steps:
    1. Login to https://console.firebase.google.com with your gmail id
    2. Add a Project
    3. Open the Project and in LHS menu, select DataBase
    4. Create DataBase may be test mode -> Cloud Firestore

    Accessing Firestore from Python
    1. Install firebase-admin library
    2. In Project Settings Go to Serivce Accounts Tab and download config file
    3. In Python Porgram write your object to be saved and use firebase code i.e. API's to perform DB Operations

"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class Dish:

    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating


    def show_dish(self):
        print("-------------------------------------")
        print("|  {}  |  {}  |  {}  |".format(self.name, self.price, self.rating))
        print("-------------------------------------")

    def to_dictionary(self):
        return {
            'name': self.name,
            'price': self.price,
            'rating': self.rating
        }


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

    def to_dictionary(self):
        return {
            'title': self.title,
            'num_of_dishes': self.num_of_dishes,
        }


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


    def to_dictionary(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'address': self.address,
            'description': self.description,
            'ratings': self.ratings,
        }

def main():

    # Intialize Firebase App which serves as connection to the Firebase for our Usage :)
    cred = credentials.Certificate('firebase-key.json')  # PS: firebase-key.json to be downloaded aas a file and to be saved in your python project
    firebase_admin.initialize_app(cred)
    print("Firebase Initialized")

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

    # Get the data as Dictionary from Object
    data_to_save = restaurant.to_dictionary()
    print(data_to_save)

    menu_data = restaurant.menu.to_dictionary()
    print(menu_data)

    dishes = restaurant.menu.dishes

    # 1. Save data in Firebase
    db = firestore.client() # Get the reference to firestore database

    # db.collection('restaurants-py').add(data_to_save)
    # db.collection('restaurants-py').document('7b9s4wjB8h6dOznlW2XK').collection('menu').add(menu_data)

    """
    for dish in dishes:
        dish_data = dish.to_dictionary()
        db.collection('restaurants-py').document('7b9s4wjB8h6dOznlW2XK')\
            .collection('menu').document('EyHyuJz2E8T6cppYVAhJ')\
            .collection('dishes').document(dish.name).set(dish_data) # set will also insert/update the data for us :)
        print(dish.name, "Saved")

    print("Data Saved :)")
    """

    """
    dish = Dish(name="Sandwich", price=120, rating=4.7)
    dish_data = dish.to_dictionary()

    db.collection('restaurants-py').document('7b9s4wjB8h6dOznlW2XK') \
        .collection('menu').document('EyHyuJz2E8T6cppYVAhJ') \
        .collection('dishes').document(dish.name).set(dish_data)

    print("Dish Data Updated")
    """

    """
    db.collection('restaurants-py').document('7b9s4wjB8h6dOznlW2XK') \
        .collection('menu').document('EyHyuJz2E8T6cppYVAhJ') \
        .collection('dishes').document('Samosa').delete()
    print("Document Deleted")
    """

    documents = db.collection('restaurants-py').document('7b9s4wjB8h6dOznlW2XK') \
        .collection('menu').document('EyHyuJz2E8T6cppYVAhJ') \
        .collection('dishes').get()

    for document in documents:
        # print(document)
        print(document.id, document.to_dict())

if __name__ == '__main__':
    main()

"""
    Assignment:
        Design an Application in Python which will be console based Cab Booking Service
        We will have 2 programs:
        Program1: User
            User can send a Request for the Cab Booking with from and to location with some type of cab
            collections:
                /users
                /requests
        Program2: Admin
            We will see all the request from the Users
                /requests
                    we will add another document for the driver
                    or we will update the document with some attribute set to true or false for request status
            If we can attach a cab to the User, we will attach/link a driver to the User, else we will reject the request


"""