"""
    Types of Inheritance
"""

# 1. Single Level Inheritance -> 1 Parent and 1 Child
class CA:       # CA is Parent or Super Class
    pass

class CB(CA):   # CB is Child of Sub Class
    pass

# 2. Multi Level Inheritance   -> Parent to Child to Grandchild
class CC(CB):   # CC is child of CB but Grandchild of CA
    pass


# 3. Hierarchy  -> 1 Parent with multiple children
class CD:
    pass

class CE(CD):
    pass

class CF(CD):
    pass

# 4. Multiple -> More than 1 Parent for a single child
class CG:
    pass

class CH:
    pass

class CI(CG, CH):
    pass

# Weekend Assignment: Look out for the real time Use Cases and implement these Inheritance techniques
# Use Case must be from PayTM :)