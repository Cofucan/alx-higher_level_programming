#!/usr/bin/python3
"""
    This module defines Node class that defines a node for a
    singly-linked list and a SinglyLinkedList class that defines a
    singly-linked list.
"""


class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data to be added to the node.
            next_node (Node): Pointer to the next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter function to retrive the value of data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter function to set the value of data.

        Args:
            value (node): value to initialize self.value with.

        Raises:
            TypeError: if value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter function to retrive the value of next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter function to set the value of next_node.

        Args:
            value (node): value to initialize self.__next_node with.

        Raises:
            TypeError: if value is not a node object.
        """
        if type(value) is not Node and (value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""

    def __init__(self):
        """Initialize the head of the list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a node to the singly linked list

        The node is inserted at a sorted position in the list.

        Args:
            value (Node): The node to insert
        """

        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head

            while (curr.next_node is not None and curr.next_node.data < value):
                curr = curr.next_node

            new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        """ For printing the list. """
        values = []
        curr = self.__head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next_node

        return '\n'.join(values)
