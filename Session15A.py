file = open("quotes.txt", "r") # r -> read mode
# file = open("Session15.py", "r") # r -> read mode
# file_content = file.read()
# print(file_content)
# print(type(file_content))

# list of lines in the file
lines = file.readlines()
print(lines)
print(type(lines))

for line in lines:
    print(line)