"""
    Built In Modules
    Exception Handling
"""

import os

print(os.name)
print(os.uname())
print(os.getlogin())
print(os.getcwd())
print(os.getppid())

path_to_directory = "/Users/ishantkumar/Downloads"
path_to_file = "/Users/ishantkumar/Downloads/larry.png"

print("Downloads Director Exists?", os.path.isdir(path_to_directory))
print("larry.png File Exists?", os.path.isfile(path_to_file))

path_to_directory = "/Users/ishantkumar/Downloads/Training/Feedback"

files = os.walk(path_to_directory)
files = list(files) # Convert the data in generator into a list

print(files)
# [0][2] -> Indexing may vary as per the data in directory
for file in files[0][2]:
    print(file)


# Assignment: Create a File Explorer App in Python
#             Take a folder as input and list all the contents as in | Videos | Images | Documents