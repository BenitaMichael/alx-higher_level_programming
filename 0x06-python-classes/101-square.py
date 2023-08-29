#!/usr/bin/python3

"""my square module."""

class Square:
    """Define sa Square."""

    def __str__(self):
        """Printing the square my way"""
        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with the following variables"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property of the length of a side of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Property of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the square position"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Area"""
        return self.__size * self.__size

    def pos_print(self):
        """Returns the printed"""
        square_pos = ""
        if not self.size:
            return "\n"
        for a in range(self.position[1]):
            square_pos += "\n"
        for a in range(self.size):
            for x in range(self.position[0]):
                square_pos += " "
            for y in range(self.size):
                square_pos += "#"
            square_pos += "\n"
        return square_pos

    def my_print(self):
        """Prints square."""
        print(self.square_pos_print(), end="")
