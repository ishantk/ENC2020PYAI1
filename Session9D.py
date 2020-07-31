# Built In Functions on String in Python

# Strings are IMMUTABLE -> They cannot be changed
# If we try to modify a String it will create a new String in the memory

name = "John Watson"

print("name is:", name)

upper_name = name.upper() # lower()

print("name now is:", name)
print("upper_name is:", upper_name)

author_name = "fionna flynn"
cap_author_name = author_name.capitalize()
print("author_name is:", author_name)
print("cap_author_name is:", cap_author_name)

#        0123456..
names = "john, jennie, jim, jack, joe"
print(names[0])            # j
print(names[len(names)-1]) # e

idx = names.index('o')
print("idx of o is:", idx)

idx = names.index('jennie')
print("idx of jennie is:", idx)

splitted_names = names.split(",")
print(splitted_names, type(splitted_names))

for name in splitted_names:
    print(name.strip()) # leading and trailing spaces can be eliminated from the String


print()

# replaced_names = names.replace('j', 'k')
replaced_names = names.replace('im', 'oa')
print(names)
print(replaced_names)

j_char_count = names.count('j', 0, len(names))
print("j occurred {} times".format(j_char_count))

essay = """This is an Essay on India. India is a great Country. India believes in democracy"""

words = essay.split(" ")
print(words)
print(len(words))

number = "100"
print(number, type(number))

print(number.isdigit())

if number.isdigit():
    n = int(number)
    print("n is:", n)

files = ["song1.mp3", "song2.mp3", "image1.jpg", "image2.jpg", "video1.mp4"]

print("Files which can be played by media player:")
for file in files:
    if file.endswith(".mp3") or file.endswith(".mp4"):
        print(file)

messages = [
    "hi, This is John",
    "Hello, I am doing good",
    "hi, lets catch up in evening",
    "lets talk by noon",
    "we can go for a walk",
    "we can let our computer to go on an update",
]

print()

search_keyword = "let"
print("Filtering Messages Starting with", search_keyword)
for message in messages:
    if message.startswith(search_keyword):
        print(message)
print()

print("Filtering Messages containing", search_keyword)
for message in messages:
    if search_keyword in message:
        print(message)
