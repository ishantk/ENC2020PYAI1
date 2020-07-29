# keyword arguments
# **kwargs
# **anyName -> kwargs can be any name of your choice

def employee_details(**kwargs):
    print(kwargs)
    print(type(kwargs))



employee_details(name="John", age=30, salary=30000, email="john@example.com")


def show(*args, **kwargs):
    print(args)
    print(kwargs)


show(10, 20, 30, 40, 50, name="John", phone="99999 11111", email="john@example.com")
show("kim", 10, "joe", 20, 30.22, name="John", phone="99999 11111", email="john@example.com")