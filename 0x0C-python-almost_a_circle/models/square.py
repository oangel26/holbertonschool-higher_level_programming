#!/usr/bin/python3
"""Module that represents the square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a an square and inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for square instances"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.__size = size

    def __str__(self):
        """str method for square instances"""
        super().__str__()
        msg = "[{}] ({}) {}/{} - {}"
        return msg.format(self.__class__.__name__, self.id, self.x,
                          self.y, self.__size)

    def update(self, *args, **kwargs):
        """Public method that assigns attributes to square instance"""
        if args is not None:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Public method that returns the dictionary
        representation of a Square
        """
        return {'id': self.id, 'size': self.__size,
                'x': self.x, 'y': self.y}
