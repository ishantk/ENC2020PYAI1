# Nested Functions

def hello():
    print("This is hello")


    # Nested Function: Function in a Function
    # Also known as local function
    # Sometimes, we need to write an algorithm which may execute some other function
    # if we create a local function, it will be created upon execution of the outer function
    # and shall be destroyed when execution of outer function finishes
    # Memory Level Optimization
    def bye():
        print("This is bye")

    print(bye)
    bye()

print(hello)
hello()