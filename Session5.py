"""
    Working with Loops
    COVID-19 use Case: Search, Sort and Filter Operations on Data

"""

# Loops in Elevators
start_floor = 1
total_floors = 10
# my_floor = int(input("Whats Your Floor Number: "))
my_floor = 3

for floor in range(start_floor, total_floors+1):
    print("Elevator has Reached Floor#{}".format(floor))

    if floor == my_floor:
        print("Floor Reached. Please Get Down !")
        break # Terminates the Loop

# PS: elevator Algorithm must be explored for various use cases by you
#     Consider we have 2 elevators in a building of 10 floors
#     write all the possible combinations how they will work if we have n people moving to n-floors may be up or down both parallely

num = 5
for i in range(1, 11):

    if i<5:
        continue # skips the statements in the loop to be executed below it and take the loop to next iteration

    print("{} {}'s are {}".format(num, i, num*i))


driver1 = {
                "name": "John",
                "status": 0,
                "distance": 5
          }

drivers = [
            driver1,
            {
                "name": "Jennie",
                "status": 0,
                "distance": 3
            },
            {
                "name": "Fionna",
                "status": 1,
                "distance": 15
            },
            {
                "name": "Sim",
                "status": 1,
                "distance": 4
            },
            {
                "name": "Kia",
                "status": 1,
                "distance": 3,
            }
        ]

print("DRIVERS LIST")
print(drivers)

# SORT THE LIST OF DRIVERS
n = len(drivers)

for i in range(0, n):
    for j in range(0, n-i-1):
        if drivers[j]["distance"] > drivers[j+1]["distance"]:
            # swap the elements
            drivers[j], drivers[j+1] = drivers[j+1], drivers[j]

print("SORTED DRIVERS LIST")
print(drivers)

customer = {
    "name": "Dave",
    "phone": "99999 11111",
    "email": "dave@example.com",
    "distance": 5       # look for a THE FIRST driver which is less than or equal to 5 kms
}

for i in range(len(drivers)):   # range by default starts from 0

    if drivers[i]["status"] == 0:
        continue

    if drivers[i]["distance"] > customer["distance"]:
        continue

    print("Driver Found and Details Sent:", drivers[i]["name"])
    print("Dear", customer["name"], "Your Cab Booked: SMS Sent on", customer["phone"])
    print("Dear", customer["name"], "Your Cab Booked: EMAIL Sent on", customer["email"])
    drivers[i]["status"] = 0

    break