"""
    Persistence
        Saving data permanently somewhere on computer
        1. Files eg: .txt, .csv, .html, .pdf etc...
        2. Local DataBase (DB in our system)
            MySQL, MongoDB etc..
        3. Cloud DataBase (DB in some server space)
            Google Firebase Firestore :)

"""

# Data associated in Program is Saved in RAM
# RAM is temporary. We must save the meaningful data for our data management.

choice = "yes"
# file = open("quotes.txt", "w") # w -> will over-write the previous data
file = open("quotes.txt", "a") # a -> will append current data with previous data


while choice == "yes":
    quote = input("Enter Quote: ")
    print("You Entered:", quote)
    file.write(quote)
    file.write("\n") # new line character to save next quote in next line :)
    print("quote saved:) ")

    print()
    choice = input("Add Another Quote(yes/no): ")

# Lets See files in action


