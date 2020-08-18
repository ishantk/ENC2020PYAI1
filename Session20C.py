# Passing Functions as Inputs to Other Functions

def login_with_google():
    print("Please Enter Google Credentials")

def login_with_facebook():
    print("Please Enter Facebook Credentials")

def login_with_github():
    print("Please Enter Github Credentials")


def login(login_type):
    login_type()


print("~~~~~~~~~~~~~~~~~~~~~~~")
print("1. Login With Google")
print("2. Login With Facebook")
print("3. Login With Github")
print("~~~~~~~~~~~~~~~~~~~~~~~")

choice = int(input("Please Select Login Type: "))
if choice == 1:
    login(login_with_google) # Function as Input
elif choice == 2:
    login(login_with_facebook) # Function as Input
elif choice == 3:
    login(login_with_github)  # Function as Input
else:
    print("Enter a Valid Choice")