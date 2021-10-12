#!/usr/bin/python3
""" Module that represents class BaseGeometry """


class BaseGeometry:
    """ Class that represents the BaseGeometry """

    def area(self):
        """ Public instance method: that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
