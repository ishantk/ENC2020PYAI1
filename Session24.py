"""
    Tree Data Structure
        BST | binary search tree
              property: small child in left, same or large child in right
              property: small child in left, large child in right, data must be unique

         Review below online :)
         B-Tree
         AVL Trees
         Red Black Trees
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


class TreeNode:
    def __init__(self):
        self.object = None # Object to be added is basically the key i.e. it must be unique
        self.left = None
        self.right = None

    def show_node(self):
        self.object.show_product_details()


class Tree:

    def __init__(self):
        self.root_node = None
        print("Tree Data Structure Created")

    def add(self, node, object):

        if node == None:
            node = TreeNode()
            node.object = object
            print("Node Added at Root :)")
            return node

        if object.price < node.object.price:
            node.left = self.add(node.left, object)
        else:
            node.right = self.add(node.right, object)

        return node

    def get_min1(self):
        temp = self.root_node

        while temp.left != None:
            temp = temp.left

        temp.object.show_product_details()

    def get_min2(self, node):

        if node != None:
            if node.left == None:
                node.object.show_product_details()

            self.get_min2(node.left)


    def get_max1(self):

        temp = self.root_node

        while temp.right != None:
            temp = temp.right

        temp.object.show_product_details()

    def get_max2(self, node):

        if node != None:
            if node.right == None:
                node.object.show_product_details()

            self.get_max2(node.right)

    # Iterate and find the product with given id and algo must be recursive :)
    def search(self, node, product_id):
        pass

    # Draw Recursive Stack and share it in whats app group
    def pre_order(self, node):
        if node != None:
            node.object.show_product_details() # ROOT
            self.pre_order(node.left)          # LEFT
            self.pre_order(node.right)         # RIGHT


def main():
    product1 = Product(101, "iPhoneX", 50000)
    product2 = Product(201, "Samsung LED", 60000)
    product3 = Product(301, "Oppo F1", 10000)
    product4 = Product(401, "Adidas Alphbounce", 6000)
    product5 = Product(501, "Hitachi Fridge", 70000)

    tree = Tree()
    tree.root_node = tree.add(node=None, object=product1)
    tree.add(node=tree.root_node, object=product2)
    tree.add(node=tree.root_node, object=product3)
    tree.add(node=tree.root_node, object=product4)
    tree.add(node=tree.root_node, object=product5)

    print()

    # tree.get_min1()
    tree.get_min2(tree.root_node)
    print()

    # tree.get_max1()
    tree.get_max2(tree.root_node)

    print()
    print("PRE-ORDER TRAVERSAL :)")
    tree.pre_order(tree.root_node)

if __name__ == '__main__':
    main()

"""
        
        50000 (Root Node) 
         / \
        /   \
    10000   60000 (node)
     / \      / \
    /   \    /   \
 6000  none none 70000 (Leaves)
 
 Tree Terminologies -> Please refer online exploration here :)
 Assignment: Draw Recursive Stack of the above program and share the same in whatsapp group !!
 
 Pre  Order Traversal
    R' L R   
    50000 -> 10000 -> 6000 -> 60000 -> 70000
 Post Order Traversal
    L R R'
 In Order Traversal
    L R' R
    
 Conclusion -> Which Traversal in BST will be giving the Sorted Data as Output :)   
"""