#!/usr/bin/python3
"""
    Defines a class Rectangle from Base Model.
"""
from models.base import Base


class Rectangle(Base):
    """
        Defines a Rectangle implements Base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initializes the class

            Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): Rectangle x coordinate.
            y (int): Rectangle y coordinate.
            id (int): The unique identity of the new Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Returns: width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            Returns: height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns the area of the Rectangle.
        """
        return (self.__width * self.__height)

    def display(self):
        """
            prints the standard output of the Rectangle '#'
        """
        rectangle = ""
        print_symbol = "#"

        print("\n" * self.y, end="")

        for i in range(self.height):
            rectangle += (" " * self.x) + (print_symbol*self.width) + "\n"
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """
            Updates the Rectangle
            Args:
                *args -  variable number of none keyword args
                **kwargs - variable number of keyworded args ie key-value pairs
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            returns the dictionary representation  of rectangle
        """
        return {'x': getattr(self, "x"), 'y': getattr(self, "y"),
                'id': getattr(self, "id"), 'height': getattr(self, "height"),
                'width': getattr(self, "width")}
    
    def __str__(self):
        """
            returns a string formart of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
