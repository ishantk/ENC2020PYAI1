# String Formatting
app_name = "WhatsApp"
users = 1000

print("Welcome to", app_name)
print("Welcome to %s" %(app_name)) # kind of c language syntax

print("Welcome to", app_name, "we have got", users, "users")
print("Welcome to {} we have got {} users".format(app_name, users))

num1 = 10
num2 = 3
num3 = num1 / num2
print("result is:", num3)
# Assignemnt: format the output as a string upto 2 decimals | 3.33