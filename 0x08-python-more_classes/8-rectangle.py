#!/usr/bin/python3
""" Module which creates a blueprint model for class Rectangle """


class Rectangle:
    """ class that defines a rectangle """


    number_of_instances = 0
    print_symbol = "#"


    def __init__(self, width=0, height=0):
        """ Constructor of the rectanglangle objects

        Args:
        width (int): width of rectangle.
        height (int): height of rectangle

        Raises:
        ValueError: if width or heigth is < 0.
        TypeError: if width or heigth are not integers.

        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif type(value) is int and value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Public instance method that returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ Public instance method that returns the rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            s = (((self.__width * str(self.print_symbol)) + "\n") *
            (self.__height - 1))
            s += (self.__width * str(self.print_symbol))
            return s

    def __repr__(self):
        s = (str(self.__class__.__name__) +
        '(' + str(self.__dict__['_Rectangle__width']) + ', '
             + str(self.__dict__['_Rectangle__height']) + ')')
        return s

    def __del__(self):
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

        
if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")


    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")
