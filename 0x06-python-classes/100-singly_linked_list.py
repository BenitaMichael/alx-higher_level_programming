#!/usr/bin/python3
"""module for a singly linked list"""


class Node:
    """"Defines a node"""

    def __init__(self, data, next_node=None):
        """initializes the node"""

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets data attribute"""

        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets data attribute"""

        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Gets next_node attribute"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets value of next node"""

        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')

        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        self.head = None

    def __str__(self):
        """Prints list"""

        print_ll = ""
        location = self.head
        while location:
            print_ll += str(location.data) + "\n"
            location = location.next_node
        return print_ll[:-1]

    def sorted_insert(self, value):
        """Inserts in node"""
        val = Node(value)
        if not self.head:
            self.head = val
            return
        if value < self.head.data:
            val.next_node = self.head
            self.head = val
            return
        location = self.head
        while location.next_node and location.next_node.data < value:
            location = location.next_node
        if location.next_node:
            val.next_node = location.next_node
        location.next_node = val
