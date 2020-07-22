"""

    We solve Problems of the world in CS with Architectures:
        > MVC | Model View Controller

    MODEL
        Data Storage Component in Problem Solving Architecture

        Single Value Containers
            int
            float
            str

        Multi Value Containers
            tuple
            list
            set
            dictionary

            objects : will see in our future discussion
    VIEW

        User Interface
            Textual -> Console Based
            with Visual -> Screens or Windows with widgets

    CONTROLLER
        Logical Part
        eg: Computation

"""
# Textual -> Console Based
# Anything on UI, will be read as a string and is displayed as a string
name = input("Whats Your Name? ")
# age = input("Whats Your Age? ")
age = int(input("Whats Your Age? "))

# PS: you must convert the data from user into the types which you are expecting
#     int, float, str

print(type(name))
print(type(age))

print("Hello,", name)
print("You are as of now {} years old".format(age))

# Add 3 in Age and update the value of Age
age = age + 3
print("You will be {} years old after 3 years".format(age))

# Textual UI
# input -> to read data from User
# print -> to show data to User