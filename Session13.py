"""
    Inheritance
        What is Inheritance ?
            Its a relationship between 2 types
            Rule: Whatever is in the Parent is accessible by Child, if not available with Child
        Why we need Inheritance ?
            If we closely observe the Rule of Inheritance, we can re-use the Code
"""

class Parent:
    # init is executed whenever object of Parent is created in the memory
    def __init__(self):
        print("Parent Object Constructed")

        # we will write data in object
        self.fname = "John"
        self.lname = "Watson"
        self.wealth = 100000

    def show(self):
        print("This is show of Parent")


# Inheritance Relationship | class CA: pass     class CB(CA): pass | CA is Parent and CB is Child
class Child(Parent):

    # def __init__(self):
    #     print("Child Object Constructed")


    # Re-Define the same function in Child which is available in Parent
    # Overriding
    def show(self):
        print("This is show of Child")



def main():

    # pRef = Parent()
    # pRef.show()

    print("Parent Class Dictionary")
    print(Parent.__dict__)

    print("Child Class Dictionary")
    print(Child.__dict__)

    # Constructor will be executed
    # If not available in the Child, Parent's constructor shall be used :)

    # Rule of Inheritance:
    # Child will access Parent's Property if not available within the Child
    # if available, it will execute its own :)

    cRef = Child()  # cRef is Ref Var which holds hashcode of object and will be passed to the self in the class functions

    print("cRef Dictionary:")
    print(cRef.__dict__)

    cRef.show()


if __name__ == '__main__':
    main()