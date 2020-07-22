# dictionary also known as map or hashmap
# stores the data as key value pair
# Remember, key and value can be any type of your choice
# most of the times we tend to keep keys as strings only

restaurant = {
    "name": "Gopal Sweets",
    "reviews": 4.3,
    "categories": ["Mithai", "Indian", "Bakery", "Fast Food"],
    "time_to_deliver": 35,
    "price_per_person": 150,
    "promo_code": "CRAVINGS25"
}

restaurant["address"] = "Sarabha Nagar"
restaurant["phone"] = "90909 12121"

print(restaurant)
print(type(restaurant))
print(len(restaurant))

dish1 = {
    "name": "Gujiya",
    "price": 125
}

dish2 = {
    "name": "Khoya Burfi",
    "price": 150
}

dish3 = {
    "name": "Milk Cake",
    "price": 200
}

dishes = [dish1, dish2, dish3]
restaurant["dishes"] = dishes

print("RESTAURANT")
print(restaurant)

# Data Structures can be mixed and used as per our requirement :)

# Assignment: Represent COVID-19 Data in MVC's in Python
#             Reference Link: https://www.covid19india.org/