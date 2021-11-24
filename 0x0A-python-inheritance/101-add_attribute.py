#!/usr/bin/python3
"""Module with function that adds attribute"""
MyClass = __import__('101-main').MyClass


class NewClass(MyClass):
    
    def __init__(self, key_name
                 
    def add_attribute(obj, key_name, name):
    """Function that adds a new attribute to an object if it’s possible"""
    obj.key_name = name


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
