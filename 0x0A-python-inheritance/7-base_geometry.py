#!/usr/bin/python3
""" Module that represents class BaseGeometry """


class BaseGeometry:
    """ Class that represents the BaseGeometry """

    def area(self):
        """ Public instance method: that raises an Exception
        with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value

        Args:
        name: (str) name of integer
        value: (int) integer to validate

        Raises:
        * If value is not an integer: raise a TypeError exception
        * if value is less or equal to 0: raise a ValueError exception
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == "__main__":
    bg = BaseGeometry()

    bg.integer_validator("my_int", 12)
    bg.integer_validator("width", 89)

    try:
        bg.integer_validator("name", "John")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("age", 0)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        bg.integer_validator("distance", -4)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
