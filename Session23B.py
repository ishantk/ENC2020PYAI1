"""
    Data Structures:
    1. DoublyLinkedList
    2. Stack
    3. Queue
    4. Tree

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

# FIFO -> First In First Out
class Queue:

    # size is property of LinkedList class
    size = 0

    def __init__(self):
        print("Linked List Created")
        self.head = None
        self.tail = None

    def push(self, element):

        Queue.size += 1

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
        return Queue.size

    def iterate_forward(self):

        temp = self.head

        while temp.next != self.head:
            temp.show_product_details()
            temp = temp.next

        temp.show_product_details()

    # Remove the Head from List :)
    def poll(self):
        # Shifting the Head
        self.head = self.head.next

        # Circular Links
        self.head.previous = self.tail
        self.tail.next = self.head

    def peek(self):
        return self.head


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
    shoppingCart = Queue()
    shoppingCart.push(product1)
    shoppingCart.push(product2)
    shoppingCart.push(product3)
    shoppingCart.push(product4)
    shoppingCart.push(product5)

    print()

    shoppingCart.poll()
    shoppingCart.poll()

    print("Iterating Forward in Shopping Cart")
    shoppingCart.iterate_forward()





if __name__ == '__main__':
    main()