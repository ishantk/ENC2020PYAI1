"""
    Exploring Sequences in Python
    Sequence : Multi Value Container
               data of same type : homo
               data of diff type : hetro

               1. tuple
               2. list
               3. set
               4. dictionary
               5. string

    In CS, we know them as data structures

    Operations on Sequences:
    1. Concatenation            [t, l]
    2. Repetition               [t, l]
    3. Membership Testing       [t, l, s]
    4. Indexing                 [t, l]
    5. Slicing                  [t, l]

    They may work with few sequences and may not for others

    Iterations:
        for loop with index     [t, l]
        enhanced for loop       [t, l, s]

"""

# students = ("john", "jennie", "jim", "jack", "joe")
students = ["john", "jennie", "jim", "jack", "joe"]
# students = {"john", "jennie", "jim", "jack", "joe"}
print("students:", students, type(students))

print()

# 1. Concatenation
#    its gonna give us a new tuple in result
#    tuple is IMMUTABLE
# more_students = students + ("fionna", "dave", "sia")
more_students = students + ["fionna", "dave", "sia"]
# more_students = students + {"fionna", "dave", "sia"}
print("students:", students, type(students))
print("more_students:", more_students, type(more_students))

print()

# 2. Repetition
repeated_students = students * 3
print("students:", students, type(students))
print("repeated_students:", repeated_students, type(repeated_students))

# 3. Membership Testing | in and not in
print("john" in students)
print("leo" not in students)

# 4. Indexing
print(students[0])      # from the beginning
print(students[-1])     # form the ending

# 5. Slicing
print(students[0:3])                # from 0 to less than 3 i.e. 2
sliced_students = students[3:]      # from 3 to length i.e. 4
print("sliced_students:", sliced_students, type(sliced_students))
print(students[:3])                 # from 0 to less than 3 i.e. 2
# explore -> negative slicing
print(students[-3:-1])              # from -3 to -2 i.e. less than -1


# Read All the elements with Loops
# for i in range(0, len(students), 1):
for i in range(len(students)):
    print(students[i], end=" <--> ") # print in the same line by putting space in the end

print()

# Enhanced For Loop
# no index management, data is automatically picked 1 by 1 from the tuple :)
for student in students:
    print(student, end=" ^^^^ ")

# Explore for list and set
# tuple -> ()
# list ->  []
# set  ->  {}

# will be back by 10:10 AM IST
# code and explore and put your answers on the chat