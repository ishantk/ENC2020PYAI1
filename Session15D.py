# Random Access in Files:)

file = open("orders-11-8-2020.csv", "r")

# tell function tells the current position of cursor in file
print("Cursor:", file.tell())

# read 1st 10 chars in file
data = file.read(10)
print(data)

print("Cursor:", file.tell())

# Move the Cursor to 20th character
file.seek(20)
data = file.read(10)
print(data)

print("Cursor:", file.tell()) # 30

