# Conditional Operators
# ==, !=, >, >=, <, <=

# Logical Operators
# and, or

# Membership Operators
# is, is not

cab_fare = 575
wallet = 300

print("Can i Book the Cab:", cab_fare <= wallet)

email = "john.watson@example.com"
password = "john@123"

print("Email Auth:", (email == "john.watson@example.com"))
print("Pass Auth:", (password == "john@123"))

print("User Auth for Home Page:", (email == "john.watson@example.com") and (password == "john@123"))

otp_sent = 3027
user_otp = int(input("Enter OTP Received: "))

print("OTP MATCHED:", otp_sent == user_otp)

is_internet_enabled = True
is_GPS_enabled = False

print("Can i Use App to Login", is_internet_enabled)

print("Can i Navigate using Google Maps", is_internet_enabled and is_GPS_enabled)

# Membership Testing
a = 10
print(a == 10)
print(a is 10)

name = "Fionna"
print(name == "Fionna")
print(name is "Fionna")

print(name != "John")
print(name is not "John")

# is and == performs same operation in above use case
# explore : what is the difference between == and is
#           hashing :)
