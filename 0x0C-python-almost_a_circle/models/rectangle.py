#!/usr/bin/python3
"""Module that represents a Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class that models and represents a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of rectangle instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Public method that returns the area of the Rectangele"""
        return(self.__width * self.__height)

    def display(self):
        """
        Public method that prints in stdout the Rectangle instance
        with the character #
        """
        for k in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x, end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Method that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        msg = "[{}] ({}) {}/{} - {}/{}"
        return msg.format(self.__class__.__name__, self.id, self.__x,
                          self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Public method  that assigns an argument to each attribute"""
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation
        of a Rectangle
        """
        return {'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x, 'y': self.__y}


if __name__ == "__main__":
    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
