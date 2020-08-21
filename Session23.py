"""
    Data Structures:

    Linear Data Structures
        1. DoublyLinkedList
        2. Stack
        3. Queue

    Non Linear Data Structures
        4. Tree :)
        5. Graph

    For optimally accessing the data -> we must put it in a data structure
    eg: ShoppingCart is a Data Structure
        MusicPlayList is a Data Structure

    In order to explore more: -> https://github.com/ishantk/DSA2020-1

"""

class Product:

    def __init__(self, pid, name, price, quantity=1):
        self.pid = pid
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_product_details(self):
        print("^^^^^^^^^^^^^^^^^^^^^")
        print(self.pid, self.name)
        print(self.price, self.quantity)
        print("^^^^^^^^^^^^^^^^^^^^^")


class LinkedList:

    # size is property of LinkedList class
    size = 0

    def __init__(self):
        print("Linked List Created")
        self.head = None
        self.tail = None

    def append(self, element):

        LinkedList.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
            print("Element Added as Head :) ")
        else:
            element.previous = self.tail
            self.tail.next = element

            self.tail = element

            # Maintains Circular Links :)
            element.next = self.head
            self.head.previous = self.tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def get_size(self):
        return LinkedList.size

    def iterate_forward(self):

        temp = self.head

        while temp.next != self.head:
            temp.show_product_details()
            temp = temp.next

        temp.show_product_details()

    def iterate_backward(self):

        temp = self.tail

        while temp.previous != self.tail:
            temp.show_product_details()
            temp = temp.previous

        temp.show_product_details()

    def delete_head(self):
        pass

    def delete_tail(self):
        pass

    # check for element id i.e. product id and delete it
    def delete_element(self, element):
        pass

    # based on the prices of products :)
    # bubble sort, insertion sort :)
    def sort_list(self):
        pass

def main():
    product1 = Product(101, "iPhoneX", 50000)
    product2 = Product(201, "Samsung LED", 60000)
    product3 = Product(301, "Oppo F1", 10000)
    product4 = Product(401, "Adidas Alphbounce", 6000)
    product5 = Product(501, "Hitachi Fridge", 70000)

    """
    # Python's Built in Doubly Linked List :)
    shoppingCart = []
    shoppingCart.append(product1)
    shoppingCart.append(product2)
    shoppingCart.append(product3)
    shoppingCart.append(product4)
    shoppingCart.append(product5)
    """

    # Our Doubly Linked List Object :)
    shoppingCart = LinkedList()
    shoppingCart.append(product1)
    shoppingCart.append(product2)
    shoppingCart.append(product3)
    shoppingCart.append(product4)
    shoppingCart.append(product5)

    print("HEAD")
    shoppingCart.get_head().show_product_details()

    print()

    print("TAIL")
    shoppingCart.get_tail().show_product_details()

    print("Shopping Cart Size is:", shoppingCart.get_size())


    print()
    print("Iterating Forward in Shopping Cart")
    shoppingCart.iterate_forward()

    print()
    print("Iterating Backward in Shopping Cart")
    shoppingCart.iterate_backward()



if __name__ == '__main__':
    main()