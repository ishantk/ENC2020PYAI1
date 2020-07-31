"""
    Strings in Python
"""

# restaurant_name = 'Johns Cafe'
# restaurant_name = 'John\'s Cafe'
# restaurant_name = 'John's Cafe' # error

# restaurant_name = "John's Cafe"

# raw strings: begins from r or R
# considers escape sequences as part of your data
restaurant_name = r'John\'s Cafe'

print(restaurant_name)

print()

# Reference: for escape sequences https://linuxconfig.org/list-of-python-escape-sequence-characters-with-examples
# quote = "work hard\nget luckier"
quote = R"work hard\nget luckier" # raw string -> \n is now part of data :)
print(quote)

# Here for developer string can be written in multiple lines
message = "We are learning Python" \
          "This is an Awesome Day" \
          "Lets Code"
# but, it is a single line string for us, not a multi line
print(message)

print()

# Multi Line String
my_message = """Do attempt your assignment
and share your work on 
whatsapp group
thanks
"""

print(my_message)