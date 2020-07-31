# operations on Strings
#       012345678910
name = "John Watson"
#                 -1
print(name, type(name), hex(id(name)))

another_name = "John Watson"
print(another_name, type(another_name), hex(id(another_name)))

# Indexing
print(name[1])           # o
print(name[-2])          # o
print(name[len(name)-1]) # n

# Slicing
print(name[1:5])
print(name[5:])

reverse_name = name[::-1]
print(reverse_name)

# Concatenation
new_name = name + " Flynn"
print(new_name)

# Repetition
repeated_name = name * 2
print(repeated_name)

# Membership Testing
phone = input("Enter Your Phone Number: ")
email = input("Enter Your Email: ")


if len(phone) < 10:
    print("Invalid Phone:", phone)
else:
    print("Thank you for entering Phone:", phone)

if "@" in email and '.' in email:
    print("Thank you for entering Email:", email)
else:
    print("Invalid Email:", email)
