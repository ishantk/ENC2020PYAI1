# global variable, available to other functions as read operation
# if we wish to perform write/update operation we must use a keyword global
number = 10

"""
def show():
    # local variable and is created in show function frame
    number = 20 # number here is created within show frame :)
    print("1. number is", number)   # 20
    
"""

def show():
    global number   # use the number available above and do not create a new number
    number = 20     # manipulates global variable
    print("1. number is", number)  # 20


show()
print("2. number is", number)       # 20